# The fraud angle: making the support chat the fraud team's front door

**22nd September 2026.** Brainstormed with the product brainstorming and "ideas for an existing product" skills (PM, designer and engineer perspectives), then converged.

## Why fraud belongs here

- US consumers reported about **$16 billion** in fraud losses in 2025, a record and 25% more than 2024. Impersonation scams alone were **$3.5 billion**, with about **$1 billion** from people pretending to be a business or a bank (FTC, June 2026)
- In the UK, banks must reimburse victims of authorised push payment scams (customers tricked into sending money themselves) for payments made on or after 7th October 2024. Stopping a scam mid-conversation is now a direct cost saving there
- Support chat is where victims turn up, often **while the scam is still running**: "someone from the bank called and told me to move my money to a safe account". Fraud and support usually sit in separate teams, and the handover between them is slow

**The honest limit:** Warmhand has no transaction data, so it can't do transaction monitoring or risk scoring. That's a different discipline (machine learning on payment streams) and stays out of scope. What it *can* do is detect fraud **signals in the conversation** and get the fraud team moving faster, with a case file instead of a chat log.

## Ideation, three perspectives

| Perspective | Ideas |
|---|---|
| **PM** | 1. Detect scams in progress and interrupt them. 2. A dedicated fraud queue, separate from general support. 3. A structured fraud intake note so analysts start with a case file. 4. A fraud recall gate in the eval set. 5. Fraud specific help articles ("what we will never ask you") |
| **Designer** | 6. A "stop" message for scams in progress: short, calm, one action. 7. Never ask the victim to repeat the story. 8. Answer "is this text really from you?" safely, since it's the most common fraud *question*. 9. No blame language ("you should have..."). 10. Tell the customer what happens next without promising money back |
| **Engineer** | 11. A fraud intake schema filled by the model, with "unknown" allowed and guessing forbidden. 12. A fraud keyword net (safe account, gift card, remote access, crypto ATM, "someone from the bank"). 13. Priority routing: an urgent label plus a high priority conversation. 14. Social engineering detection aimed at the *bot*: third parties, "I'm from Kettlewick IT", requests to skip verification. 15. A separate lab on public synthetic transaction data (for example PaySim) for transaction fraud models |

## The top five, adopted

| # | Idea | Why it made the cut | Assumption to test |
|---|---|---|---|
| 1 | **Scam in progress interrupt** (ideas 1, 6, 12, 13): a fixed "stop" template (T7), an urgent label and high priority | The highest value moment in the whole product. Seconds matter, and it costs almost nothing to build | The model plus the keyword net catch paraphrased scam stories. Gold set cases test it |
| 2 | **Fraud intake note** (ideas 3, 7, 11): a structured private note with fraud type, whether it's still happening, whether money was sent, how it was sent, how the scammer made contact, whether they're still in contact, and a two line masked summary. Every field allows "unknown" | Turns a chat into a case file. This is what fraud ops teams actually want | Fields can be filled from one message without guessing. Tracked against gold labels |
| 3 | **A fraud queue** (idea 2): `fraud` and `fraud-urgent` labels route to a separate team | Mirrors how banks actually organise, and makes the demo legible | Chatwoot labels or teams can drive the routing. Stage 4 check |
| 4 | **Safe scam check answers** (ideas 5, 8): "is this text really from you?" is answered from a cited help article on what Kettlewick never asks for | The one fraud case a bot *should* answer, because an instant answer protects the customer | The article covers the common patterns |
| 5 | **Social engineering defense** (idea 14): third party requests, fake staff and verification bypass attempts hand off with a `suspected-social-engineering` note. Warmhand never confirms whether an account exists | The bot is itself an attack surface. Interviewers will ask | Red team cases in Module 10 |

**Parked:** idea 15, a transaction fraud lab on synthetic data. It's a good separate portfolio project later, since it's a different skill set (ML, not agents). Not in Warmhand.

## What changes

| File | Change |
|---|---|
| `docs/escalation_policy.md` | New section 4: fraud. New template T7 (scam in progress). The fraud intake note fields |
| `prd.md` | Fraud analyst as a user. Fraud flags and actions. Priority routing. Fraud gates and gold set cases. Two of the ten help articles are fraud related. Fraud in the positioning |
| Gold set | About 8 of the 20 adversarial cases become fraud cases: scam in progress (3), account takeover (1), social engineering (2), scam check questions (2). Real CFPB fraud categories already fill part of the 40 |

**The line for the README and interviews:** "Support chat is where fraud victims show up, often mid-scam. Warmhand spots it, interrupts it, and hands the fraud team a case file, not a transcript."

## Sources

- FTC, June 2026: https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-data-show-people-reported-losing-3-point-5-billion-imposter-scams-2025
- UK Finance, APP fraud reimbursement: https://www.ukfinance.org.uk/authorised-push-payment-fraud-reimbursement
