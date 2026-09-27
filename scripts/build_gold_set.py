"""
Draw the stratified gold set from the CFPB narrative archive.

Why stratified and not random: a random sample of 120 would be dominated by
"Managing an account" and would contain almost no cases where being wrong is
expensive. The strata are chosen so the set covers the decisions that carry
legal or human cost, not the decisions that happen most often.

Strata are DISJOINT and assigned by priority, so no complaint appears twice:
  1. Reg Z billing error        (legal clock)
  2. Reg E unauthorized charge  (legal clock)
  3. Older American tagged      (vulnerability, non legal clock)
  4. Servicemember tagged       (vulnerability, non legal clock)
  5. Ambiguous middle           (everything else, where most real errors happen)

A complaint that is both Reg Z and Older American lands in Reg Z. That is
deliberate: the tag strata then test vulnerability handling on issues that do
not already force a handoff for another reason.

July and August are excluded. See data/SOURCE.md: the publication cutoff of
14th August 2026 biases them toward complaints the company answered quickly.

Output: evals/gold_set_raw.csv, which contains narrative text and is gitignored.
Label it, then scripts/split_gold_set.py (later) strips the text so only
complaint IDs and our own labels are committed.

Run: python3 scripts/build_gold_set.py
"""

import pandas as pd

SEED = 20260927
NARRATIVE = "Consumer complaint narrative"
PRODUCTS = ["Credit card", "Checking or savings account"]
COLS = ["Date received", "Product", "Sub-product", "Issue", "Sub-issue", "Tags",
        NARRATIVE, "Complaint ID"]

FILES = [
    "data/raw/CCDB_Export_17_April_2026.zip",
    "data/raw/CCDB_Export_18_May_2026.zip",
    "data/raw/CCDB_Export_19_June_2026.zip",
]

REG_Z = "Problem with a purchase shown on your statement"
REG_E = "Problem with a lender or other company charging your account"

TARGETS = [
    ("reg_z_billing_error", 25),
    ("reg_e_unauthorized", 25),
    ("older_american", 20),
    ("servicemember", 20),
    ("ambiguous_middle", 30),
]


def stratum(row):
    if row["Issue"] == REG_Z:
        return "reg_z_billing_error"
    if row["Issue"] == REG_E:
        return "reg_e_unauthorized"
    tags = row["Tags"] if isinstance(row["Tags"], str) else ""
    if "Older American" in tags:
        return "older_american"
    if "Servicemember" in tags:
        return "servicemember"
    return "ambiguous_middle"


def main():
    frames = []
    for path in FILES:
        df = pd.read_csv(path, usecols=COLS, low_memory=False)
        df = df[df["Product"].isin(PRODUCTS)]
        df = df[df[NARRATIVE].notna()]
        frames.append(df)
    pool = pd.concat(frames, ignore_index=True)
    pool = pool.drop_duplicates(subset=["Complaint ID"])
    pool["stratum"] = pool.apply(stratum, axis=1)
    pool["narrative_words"] = pool[NARRATIVE].str.split().str.len()

    print(f"Pool: {len(pool):,} complaints, April to June 2026\n")
    print("Available per stratum:")
    print(pool["stratum"].value_counts().to_string())

    picked = []
    print("\nDrawn:")
    for name, n in TARGETS:
        available = pool[pool["stratum"] == name]
        if len(available) < n:
            raise SystemExit(f"stratum {name} has {len(available)}, need {n}")
        sample = available.sample(n=n, random_state=SEED)
        picked.append(sample)
        print(f"  {name:22} {n:>3} of {len(available):,}")

    gold = pd.concat(picked, ignore_index=True)
    gold = gold.sample(frac=1, random_state=SEED).reset_index(drop=True)

    # Empty columns for the labeller. These are the asset.
    gold["label_decision"] = ""      # answer | hand_off | crisis
    gold["label_policy_section"] = ""  # e.g. 1, 2, 3, 3A, 4
    gold["label_reasoning"] = ""     # one line, in your own words

    out = "evals/gold_set_raw.csv"
    gold.to_csv(out, index=False)
    print(f"\nWrote {len(gold)} cases to {out} (gitignored, contains narrative text)")
    print(f"Seed {SEED}. Rerunning reproduces exactly this set.")
    print(f"\nNarrative length in the drawn set: median "
          f"{gold['narrative_words'].median():.0f} words, "
          f"longest {gold['narrative_words'].max():.0f}")
    print(f"Over 400 words (should hand off on length alone): "
          f"{(gold['narrative_words'] > 400).sum()} of {len(gold)}")


if __name__ == "__main__":
    main()
