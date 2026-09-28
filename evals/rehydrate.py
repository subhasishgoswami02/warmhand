"""
Rebuild the gold set's complaint text from complaint IDs.

Why this exists: evals/gold_set.csv holds complaint IDs and our labels, never the
narrative text. The labels are ours to publish. The text is the CFPB's, it names
real companies, and republishing a searchable pile of it under this repo's name is
not something we want to do. Pinning by ID keeps the set fully reproducible without
that.

IMPORTANT: the live CFPB API cannot rehydrate this. The Bureau stopped publishing
narratives on 14th August 2026, so the current database has no narrative column at
all. The text lives only in the archived monthly exports in the CFPB's FOIA
Electronic Reading Room. This script reads those.

Run: python3 evals/rehydrate.py
Needs: the three archive zips in data/raw/. It downloads them if they are missing.
Writes: evals/gold_set_rehydrated.csv (gitignored)
"""

import os
import sys
import urllib.request

import pandas as pd

BASE = "https://files.consumerfinance.gov/f/documents/"
ARCHIVES = [
    "CCDB_Export_17_April_2026.zip",
    "CCDB_Export_18_May_2026.zip",
    "CCDB_Export_19_June_2026.zip",
]
RAW = "data/raw"
LABELS = "evals/gold_set.csv"
OUT = "evals/gold_set_rehydrated.csv"
NARRATIVE = "Consumer complaint narrative"


def ensure_archives():
    os.makedirs(RAW, exist_ok=True)
    for name in ARCHIVES:
        path = os.path.join(RAW, name)
        if os.path.exists(path):
            print(f"have  {name}")
            continue
        print(f"fetch {name} ...", flush=True)
        urllib.request.urlretrieve(BASE + name, path)
        print(f"      {os.path.getsize(path) / 1e6:.0f} MB")


def main():
    if not os.path.exists(LABELS):
        sys.exit(f"{LABELS} not found. It holds the complaint IDs and the labels.")

    ensure_archives()

    labels = pd.read_csv(LABELS)
    wanted = set(labels["Complaint ID"])
    print(f"\nlooking for {len(wanted):,} complaint IDs")

    found = []
    for name in ARCHIVES:
        df = pd.read_csv(os.path.join(RAW, name),
                         usecols=["Complaint ID", NARRATIVE], low_memory=False)
        hit = df[df["Complaint ID"].isin(wanted)]
        print(f"  {name}: {len(hit)}")
        found.append(hit)

    text = pd.concat(found, ignore_index=True).drop_duplicates(subset=["Complaint ID"])
    merged = labels.merge(text, on="Complaint ID", how="left")

    missing = merged[NARRATIVE].isna().sum()
    merged.to_csv(OUT, index=False)
    print(f"\nwrote {OUT}: {len(merged)} rows, {missing} without text")

    if missing:
        print("\nSome IDs did not resolve. The likely cause is that the consumer")
        print("withdrew consent, which removes the narrative from publication.")
        print("That is expected occasionally and is why the set is pinned by ID:")
        print("the label survives even when the text does not. Report the count")
        print("rather than silently dropping those cases.")


if __name__ == "__main__":
    main()
