"""
Count the usable gold set pool in the CFPB narrative archive exports.

Why this exists: the gold set is stratified, not random. A random sample would be
dominated by the largest issue category and would contain almost none of the cases
where being wrong is expensive (Reg Z billing errors, Reg E unauthorized charges,
vulnerable customers). This script sizes each stratum so we know whether it survives
on the complete months alone.

Run:  python3 scripts/count_strata.py
Data: data/raw/CCDB_Export_*.zip  (gitignored, see data/SOURCE.md)
"""

import pandas as pd

PRODUCTS = ["Credit card", "Checking or savings account"]
NARRATIVE = "Consumer complaint narrative"
COLS = ["Date received", "Product", "Issue", "Sub-issue", "Tags", NARRATIVE, "Complaint ID"]

# The two issue categories that carry a legal clock. See docs/escalation_policy.md.
LEGAL_CLOCK = {
    "Problem with a purchase shown on your statement": "Reg Z billing error",
    "Problem with a lender or other company charging your account": "Reg E unauthorized",
}

FILES = {
    "April 2026": "data/raw/CCDB_Export_17_April_2026.zip",
    "May 2026": "data/raw/CCDB_Export_18_May_2026.zip",
    "June 2026": "data/raw/CCDB_Export_19_June_2026.zip",
    "July 2026": "data/raw/CCDB_Export_20_July_2026.zip",
}


def load(path):
    """Read one monthly export, keep our two products and rows that have text."""
    df = pd.read_csv(path, usecols=COLS, low_memory=False)
    total = len(df)
    df = df[df["Product"].isin(PRODUCTS)]
    df = df[df[NARRATIVE].notna()]
    return total, df


def main():
    parts = []
    print("=" * 70)
    print("PER MONTH")
    print("=" * 70)
    for label, path in FILES.items():
        total, df = load(path)
        df = df.assign(month=label)
        parts.append(df)
        tags = df["Tags"].value_counts().to_dict()
        print(f"\n{label}: {total:,} rows in file, {len(df):,} usable "
              f"(our products, with narrative)")
        print(f"  Older American: {tags.get('Older American', 0):,}   "
              f"Servicemember: {tags.get('Servicemember', 0):,}   "
              f"Both: {tags.get('Older American, Servicemember', 0):,}")

    pool = pd.concat(parts, ignore_index=True)
    complete = pool[pool["month"] != "July 2026"]

    for name, frame in [("APRIL TO JUNE (primary pool)", complete),
                        ("APRIL TO JULY (all usable)", pool)]:
        print("\n" + "=" * 70)
        print(f"{name}: {len(frame):,} complaints")
        print("=" * 70)

        print("\nBy product:")
        print(frame["Product"].value_counts().to_string())

        print("\nTop 12 issues:")
        print(frame["Issue"].value_counts().head(12).to_string())

        print("\nLegal clock categories:")
        for issue, rule in LEGAL_CLOCK.items():
            print(f"  {rule:22} {(frame['Issue'] == issue).sum():>6,}   ({issue})")

        print("\nVulnerability tags:")
        tags = frame["Tags"].value_counts()
        for tag in ["Older American", "Servicemember", "Older American, Servicemember"]:
            print(f"  {tag:32} {tags.get(tag, 0):>6,}")
        print(f"  {'Any tag':32} {frame['Tags'].notna().sum():>6,}")

        words = frame[NARRATIVE].str.split().str.len()
        print(f"\nNarrative length in words: median {words.median():.0f}, "
              f"mean {words.mean():.0f}, 90th percentile {words.quantile(0.9):.0f}, "
              f"max {words.max():.0f}")


if __name__ == "__main__":
    main()
