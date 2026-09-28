# Kettlewick Bank help articles

**Kettlewick Bank does not exist.** These articles are written for a fictional US bank so Warmhand has something real to retrieve from and cite. Every number, fee and process here is invented. Nothing is copied from any real bank, and nothing here is financial or legal advice.

## Why there are five and not ten

The PRD proposed ten. Five ship. The cut was made against the measured issue distribution in the gold set pool (19,569 real complaints, April to June 2026, `scripts/count_strata.py`), not against a guess about what customers might want.

| Kept | Covers | Why |
|---|---|---|
| `fees.md` | Fees or interest (1,062 complaints in the pool) | Largest genuinely answerable category |
| `statements-and-interest.md` | Managing an account, payments | Due dates and grace periods are the most common honest how-it-works question |
| `cards.md` | Freezing, replacing, limits | The one protective action Warmhand may explain during a fraud report |
| `spotting-scams.md` | Fraud | The only article Warmhand may cite in a fraud conversation, per policy 3A |
| `reaching-a-person.md` | All of it | The anti doom loop article. The CFPB's own 2023 report named doom loops as a chatbot harm |

| Cut | Why |
|---|---|
| Rewards | No safety consequence, and rewards questions are not in the top issues |
| Deposits, withdrawals and ATM limits | Limits folded into `cards.md`. The rest is low frequency |
| Closing your account | 1,358 complaints, but they are about problems closing, not how to close. Those are handoffs whatever the article says |
| How interest works, as its own article | Merged into `statements-and-interest.md`. Splitting them created two half articles that each failed to answer the real question |
| A charge you don't recognize, as its own article | The decision is always a handoff (policy section 1, Reg E and Reg Z). An article inviting Warmhand to explain a dispute was a hazard, not a help. The process is described in `reaching-a-person.md` in terms of what happens next, with no timelines quoted |

Add an article later only when a labelled gold set case shows Warmhand refusing something it should have been able to answer. That is evidence. "Users would expect it" is not.

## Deliberate gaps

These articles do **not** cover: a specific customer's balance, transaction or fee; why an application was declined; credit limit changes; disputes, timelines or liability; tax; anything about a named third party. Those gaps are the point. They give the relevance gate something to correctly refuse, and several gold set cases test exactly that.

## Rules for editing

Every sentence must be quotable on its own, because Warmhand's citations are checked in code against the verbatim text of the passage it cites. Vague sentences produce unverifiable citations. State a number or state nothing.

No sentence may promise an outcome, quote a legal deadline, or tell a customer what they are entitled to. That is policy section 5, and it holds inside the articles as firmly as in the replies.
