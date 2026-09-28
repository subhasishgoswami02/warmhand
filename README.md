# Warmhand

An AI support agent for a fictional bank, built in public, from scratch, by a product manager learning how agentic systems actually work.

The thing being tested is not whether an agent can answer questions. It is whether it knows when to stop and hand the conversation to a person.

## Status, 28th September 2026

**Nothing runs yet.** This is honest rather than modest: there is no agent in this repository today. What exists is the specification, the evaluation data and the tooling that will judge the agent once it is written.

| Piece | State |
|---|---|
| Product spec and escalation policy | Written, `prd.md` and `docs/escalation_policy.md` |
| Help articles the agent answers from | Written, `docs/help_articles/` |
| Evaluation set, real complaints | 30 cases drawn, unlabelled |
| Evaluation set, synthetic questions | 40 cases written, unlabelled |
| PII masking test set | 40 cases written |
| The agent | Not started |

Follow `course/STATE.md` for the current state. It is the only file that is kept accurate.

## The problem

When a customer writes to a bank, some messages are safe for a bot to answer and some are not. A question about the overdraft fee is fine. A disputed charge is not, because it carries a legal clock. Someone saying their husband died is not. Someone being talked through a scam while they type is emphatically not.

The CFPB's 2023 report on banking chatbots named the failures: wrong answers, failing to recognise a dispute, and doom loops where a customer cannot reach a human. Getting the handoff wrong is where the cost sits, and it is the part nobody publishes numbers on.

## What is actually here

**An escalation policy** (`docs/escalation_policy.md`) that decides when the agent may answer and when it must stop. Written as a compliance document, because the code implements it and disagreement between the two is a bug in the code.

**An evaluation set** built from the CFPB Consumer Complaint Database. Thirty real complaints, stratified so that the cases where being wrong is expensive are represented rather than swamped by the most common category, plus forty synthetic questions covering the answerable side that a regulator complaint corpus does not contain.

**A PII masking test set** (`evals/pii/`), 40 cases in two directions: does anything sensitive survive, and does anything harmless get eaten. Fully synthetic, so it is safe to publish and anyone can run it against their own masker.

## The data, and a thing worth knowing

The CFPB **stopped publishing consumer complaint narratives on 14th August 2026**. The live database and API now carry structured fields only. Narratives published before that date remain public and were moved to the Bureau's FOIA Electronic Reading Room, which is where this project's evaluation text comes from.

A consequence nobody downloading these files will notice: the final months are truncated, because a complaint is published after the company responds or after 15 days, and publication stopped mid-August. July's surviving narratives skew toward complaints companies answered quickly. This project uses April to June only and excludes the rest.

`data/SOURCE.md` has the full provenance, every measured count, and the reasoning.

## Limitations, stated up front

These are real and naming them is part of the point.

**The evaluation measures policy compliance, not policy quality.** The bank is fictional, the help articles are invented, and the escalation policy was written by the same person labelling the evaluation set. A perfect score means the agent follows the policy. It says nothing about whether the policy is correct.

**The labels are one person's judgement.** A second labeller with banking experience is being sought for a subset, and the agreement rate will be published whatever it is. Until then, treat the labels as a single informed opinion.

**The complaint corpus is a post-failure corpus.** Everyone in it already contacted their bank and escalated to a federal regulator. It contains almost no easy questions, which is why the synthetic half exists, and it would reward an agent that escalates everything if used alone.

**The narratives are written submissions, not chat messages.** Median 206 words. The evaluation is of triage on a long written complaint, not on a one line chat turn.

**Nobody asked for this test set.** It exists because building it is how the author learns the problem, and because publishing the method is more useful than publishing a claim. Adoption is not the goal.

## Reproducing the data

```bash
python3 scripts/count_strata.py     # measure the pool
python3 scripts/build_gold_set.py   # draw the 30 cases, seed 20260927
python3 evals/rehydrate.py          # rebuild complaint text from IDs
```

The evaluation set is committed as complaint IDs and labels, never as complaint text. The labels are ours to publish; the text is the CFPB's and names real companies. Pinning by ID keeps the set reproducible without republishing it.

## Built by

Subhasish Goswami, a product manager in fintech, writing the code rather than reviewing it. The commit history is part of the evidence, including the parts where it went wrong.

MIT licensed. Kettlewick Bank does not exist. Nothing here is financial or legal advice.
