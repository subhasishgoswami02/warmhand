"""
Label the gold set one case at a time, in the terminal.

Why this exists: reading a 206 word complaint inside a spreadsheet cell is
miserable, and the labelling is the one part of this project nobody else can do.
Removing the friction is the difference between it happening tonight and not
happening.

Saves after every case, so stop whenever you like and run it again to pick up
where you left off. Already labelled cases are skipped.

Run: python scripts/label.py
"""

import os
import shutil
import sys
import textwrap

import pandas as pd

SRC = "evals/gold_set_raw.csv"
NARRATIVE = "Consumer complaint narrative"
DECISIONS = {"a": "answer", "h": "hand_off", "c": "crisis"}


def show(case, n, total):
    width = min(shutil.get_terminal_size((100, 24)).columns, 100)
    print("\n" + "=" * width)
    print(f"CASE {n} of {total}   id {case['Complaint ID']}   {case['narrative_words']} words")
    print("=" * width)
    for line in str(case[NARRATIVE]).split("\n"):
        print(textwrap.fill(line, width=width) if line.strip() else "")
    print("-" * width)
    # Metadata AFTER the text, on purpose: read the complaint and decide first,
    # then see how the CFPB categorised it. Seeing the label first anchors you.
    print(f"CFPB said: {case['Product']} / {case['Issue']} / {case['Sub-issue']}")
    print(f"Tags: {case['Tags'] if isinstance(case['Tags'], str) else 'none'}")
    print(f"(drawn as: {case['stratum']})")
    print("-" * width)


def ask(case):
    while True:
        d = input("Decision  [a]nswer  [h]and_off  [c]risis  (s to skip, q to quit): ").strip().lower()
        if d == "q":
            return None
        if d == "s":
            return "skip"
        if d in DECISIONS:
            break
        print("  a, h, c, s or q please.")

    section = input("Policy section (1, 2, 3, 3A, 4): ").strip()
    while True:
        reason = input("One line, your words, why: ").strip()
        if len(reason.split()) >= 3:
            break
        print("  Three words minimum. This column is what an interviewer reads.")
    return DECISIONS[d], section, reason


def main():
    if not os.path.exists(SRC):
        sys.exit(f"{SRC} not found. Run scripts/build_gold_set.py first.")

    df = pd.read_csv(SRC)
    for col in ["label_decision", "label_policy_section", "label_reasoning"]:
        if col not in df.columns:
            df[col] = ""
        df[col] = df[col].fillna("")

    todo = df[df["label_decision"].astype(str).str.strip() == ""].index.tolist()
    done = len(df) - len(todo)
    if not todo:
        print(f"All {len(df)} cases already labelled. Run scripts/split_gold_set.py next.")
        return

    print(f"\n{done} of {len(df)} done. {len(todo)} to go.")
    print("Read the complaint, decide, then look at what the CFPB called it.")
    print("Ctrl+C or q at any point. Progress is saved after every case.\n")

    for i in todo:
        show(df.loc[i], done + 1, len(df))
        try:
            result = ask(df.loc[i])
        except (KeyboardInterrupt, EOFError):
            print("\n\nStopped. Progress saved.")
            break
        if result is None:
            print("\nStopped. Progress saved.")
            break
        if result == "skip":
            continue
        decision, section, reason = result
        df.loc[i, "label_decision"] = decision
        df.loc[i, "label_policy_section"] = section
        df.loc[i, "label_reasoning"] = reason
        df.to_csv(SRC, index=False)
        done += 1
        print(f"  saved. {len(df) - done} left.")

    remaining = (df["label_decision"].astype(str).str.strip() == "").sum()
    print(f"\n{len(df) - remaining} of {len(df)} labelled.")
    if remaining:
        print("Run it again when you want to carry on.")
    else:
        print("Done. Next: python scripts/split_gold_set.py")
        print(df["label_decision"].value_counts().to_string())


if __name__ == "__main__":
    main()
