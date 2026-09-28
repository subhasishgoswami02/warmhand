"""
Split the labelled gold set into the part that is committed and the part that is not.

In:  evals/gold_set_raw.csv   (labelled by hand, holds CFPB narrative text)
Out: evals/gold_set.csv       (complaint IDs, metadata and our labels, committed)

The narrative text never enters git. See evals/rehydrate.py for how anyone rebuilds
it from the CFPB archive.

Refuses to write if any case is unlabelled, so a half finished pass cannot be
published as if it were complete.

Run: python3 scripts/split_gold_set.py
"""

import sys

import pandas as pd

SRC = "evals/gold_set_raw.csv"
OUT = "evals/gold_set.csv"
NARRATIVE = "Consumer complaint narrative"
DECISIONS = {"answer", "hand_off", "crisis"}

KEEP = ["Complaint ID", "Date received", "Product", "Sub-product", "Issue",
        "Sub-issue", "Tags", "stratum", "narrative_words",
        "label_decision", "label_policy_section", "label_reasoning"]


def main():
    df = pd.read_csv(SRC)

    blank = df["label_decision"].isna() | (df["label_decision"].astype(str).str.strip() == "")
    if blank.any():
        sys.exit(f"{blank.sum()} of {len(df)} cases are unlabelled. "
                 f"Nothing written. Finish the pass first.")

    bad = set(df["label_decision"].str.strip()) - DECISIONS
    if bad:
        sys.exit(f"unrecognised decisions: {sorted(bad)}. Allowed: {sorted(DECISIONS)}")

    thin = df["label_reasoning"].fillna("").str.split().str.len() < 3
    if thin.any():
        print(f"warning: {thin.sum()} cases have a reasoning line under three words. "
              f"That column is what an interviewer reads.")

    out = df[KEEP].copy()
    out.to_csv(OUT, index=False)

    print(f"wrote {OUT}: {len(out)} cases, no narrative text\n")
    print(out["label_decision"].value_counts().to_string())
    print("\nBy stratum and decision:")
    print(pd.crosstab(out["stratum"], out["label_decision"]).to_string())


if __name__ == "__main__":
    main()
