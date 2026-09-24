# Warmhand PRD

**Status:** Draft v1.4, 22nd September 2026. Stage 3 done: flows, user stories and acceptance criteria in `docs/flows_and_stories.md`. v1.3 added fraud and the review fixes (`docs/reviews/2026-09-22_prd_v1.2_review.md`). Stage 3 of 4 (competitive analysis added). v1.0 was rewritten after the pivot from GitHub issue triage (v0.3 archived at `docs/archive/github/prd_v0.3.md`). Nothing is built yet except the repo skeleton.
**Owner:** Subhasish Goswami (product, build, and policy owner).

**One line:** Warmhand does the first pass on every customer message to Kettlewick Bank, answering from the bank's own help articles when it can cite them, and handing the conversation to a human, with a note explaining why, whenever money, the law, fraud or a vulnerable customer is involved.

**Descriptor:** An open reference agent and handoff benchmark for AI support in regulated banking.

**Kettlewick Bank is fictional.** Every page and message says so.

---

## 1. Summary

Warmhand is an agent behind a bank's support chat (Chatwoot). For each new customer message it masks card and account numbers, classifies the complaint, checks it against a written escalation policy (`docs/escalation_policy.md`), and then does one of two things: answers from the bank's help articles with a citation, or hands the conversation to a human with a private note so the customer never repeats themselves. Its limits live in code, so a manipulated model still can't move money, request sensitive data or promise refunds. Every decision is logged without personal data, and a nightly regression gate built from real public complaints blocks prompt changes that make it worse.

**Fraud:** support chat is where fraud victims show up, often while the scam is still running. Warmhand spots fraud signals in the conversation, interrupts scams in progress with a fixed "stop" message, and hands the fraud team a structured case note instead of a transcript.

**Operating principle:** precision over coverage. On real data, most complaints must go to a human. The job is to get those to the right person fast, with context, and answer the rest correctly.

## 2. Background and why now

**Context.** Banks are deploying AI support agents fast (Intercom Fin, Zendesk, Decagon, Sierra and banking specific assistants). In a regulated domain, the hard part isn't answering. It's knowing which conversations the bot must never own: disputes and unauthorized transactions with legal deadlines, hardship, fraud, and vulnerable customers.

**Why this domain.** The project started as GitHub issue triage and pivoted on 19th September 2026, after the competitive analysis showed that category being absorbed by the platform (`docs/pivot_change_map.md`). Bank complaints are a live market, there is real labeled public data (the CFPB complaint database), and the builder has 14 years of fintech judgment.

**Why fraud.** US consumers reported about $16 billion in fraud losses in 2025, a record, including about $1 billion to people impersonating a business or a bank (FTC, June 2026). In the UK, banks must reimburse victims of authorised push payment scams for payments since 7th October 2024, so interrupting a scam mid-conversation saves real money. Details: `docs/research/2026-09-22_fraud_angle.md`.

**Why now.** Models are now reliable enough at tool calling and structured output for a narrow, auditable agent to be built by one person. Bank support AI is crowded (Fin, Zendesk, Decagon, Sierra, Kasisto, Posh, and Chatwoot's own Captain), and the leaders already claim guardrails in code and low hallucination rates. What nobody publishes is the test set. The CFPB has said in writing what goes wrong with bank chatbots: wrong answers, failing to recognize disputes, doom loops, privacy and phishing risk. An open benchmark built from the CFPB's own public complaint data, testing exactly those failures, is unclaimed. See section 12.

## 3. Goals and non-goals

### Product goals

1. Customers with a general question the help articles answer get a correct, cited answer within a minute
2. Every conversation that needs a human reaches one with a private note naming the reason, so the customer doesn't repeat themselves
3. No conversation is ever lost: a failure means a handoff, never silence
4. Warmhand never asks for sensitive data, never promises money, never gives advice
5. Fraud reaches the fraud team within a minute, as a structured case note. A scam in progress gets a "stop" message immediately

### Builder goals

1. **Demo:** two live messages in the Kettlewick chat, one answered with a citation, one handed off with its reason visible in a private note, in under 60 seconds of recording. End of Phase A
2. **Gate:** a deliberately degraded prompt is blocked by the regression gate. Phase B
3. **Reproducible:** a stranger runs it from the README alone. Phase C
4. **Honest content:** one post per module, never claiming more than the repo shows

### Non-goals

| Non-goal | Why |
|---|---|
| Any account access, balances or transactions | No real bank, and the risk class changes completely |
| Moving money: refunds, reversals, credits, waivers | Irreversible and regulated |
| Resolving or closing conversations | Humans close. Warmhand answers or hands off |
| Multi turn conversation | One reply per conversation in V0. Follow ups go to humans |
| Languages other than English, voice, attachments | Hand off instead |
| Products beyond credit cards and checking or savings accounts | No student loans, mortgages, crypto or remittances |
| Transaction monitoring and fraud scoring | No transaction data, and it's a different discipline (machine learning on payment streams). A possible separate lab later on public synthetic data |
| Billing, multiple banks in production | No demand yet |

## 4. Problem, with evidence

From the CFPB complaint database, complaints received since 1st September 2025 (pulled 20th September 2026, details in `docs/research/2026-09-20_pre_prd_checks.md`):

| Finding | Number | Status |
|---|---|---|
| Credit card complaints in the last year | 98,125 | Observed |
| Largest credit card issue: problem with a purchase on the statement (disputes, charges not made) | 30,329 | Observed |
| Share of credit card complaints in must escalate categories under the draft policy mapping | **~56%** | Derived, depends on the mapping |
| Checking and savings complaints in the last year | 89,008 | Observed |
| Share in must escalate categories, top named sub-issues only | **at least 16%** | Derived, a floor |

**Hypotheses still open:**

| Hypothesis | Why it matters | How we check |
|---|---|---|
| A real chat inbox has far more simple questions than regulator complaints | Decides how much Warmhand can answer | Can't be observed without real traffic. Stated as a limit |
| Customers repeating themselves after a bot handoff is a major frustration | The warm note is the core value | Public CX research, Stage 2 |
| ~~Bots that "reassure" create liability~~ | **Now evidence:** the CFPB's June 2023 report says chatbots must comply with federal consumer financial law and flags failing to recognize when consumers invoke their rights | Observed, external |

## 5. Users

| User | Needs | What Warmhand gives them |
|---|---|---|
| **Customer** (primary) | A fast, correct answer, or a fast route to someone who can help | A cited answer, or a handoff message plus a colleague who already has the context |
| **Support agent** (primary) | A queue where each handoff is explained | A private note on every handoff: category, flags, the policy trigger, and the would-be reply in shadow mode |
| **Fraud analyst** (primary for fraud) | Fast notice of fraud, with the facts already gathered | A `fraud` or `fraud-urgent` queue and a structured intake note: fraud type, still happening, money sent, how it was sent, how the scammer made contact, still in contact, a two line masked summary |
| **Compliance** (policy owner) | Assurance that regulated cases never get automated answers | The escalation policy as a versioned document, enforced in code, with gate results |
| **Evaluator of this artifact** | Proof the builder can ship a production agent in a regulated domain | Public repo, eval history, decision logs, release memo |

## 6. Solution (V0)

### Identity and the live system

Warmhand is a **Chatwoot agent bot** on the Kettlewick inbox, running on Chatwoot Cloud (Startups plan, starting with the 15 day trial). New conversations arrive as "pending" (the bot's queue). A handoff moves them to "open" (the human queue).

The customer reaches the chat through a one page **Kettlewick Bank help site** built in Lovable with the Chatwoot widget embedded. It says "fictional bank, demo only" at the top.

### Events

| Event | Why |
|---|---|
| New incoming message from a customer | The main path |
| Any later message from the customer in the same conversation | Only to hand off (rule 7) |

Ignored: agent messages, private notes, the bot's own messages, other inboxes.

### Pre-processing, in code, before the model

- Mask card numbers (with a checksum test), account and routing numbers, emails and phone numbers
- Keyword net: any trigger word from policy sections 1 to 3A forces a handoff, whatever the model later says

**Classification always runs**, on every message, so the model net always reads it. (v1.2 skipped the model when no help article matched, which meant a paraphrased crisis or scam story could get a generic reply. Fixed in v1.3.)

**Relevance gate, answer step only:** for "may answer" categories, search the help articles before drafting. If no article scores above the threshold, hand off **without the model writing an answer** (zero chance of an invented answer)

### Classification

**Category**, a reduced version of the CFPB taxonomy so gold set labels map one to one:

| Category | Default |
|---|---|
| Dispute or unauthorized transaction | Hand off (T2 or T1) |
| Fraud or identity theft (unauthorized use already happened, account opened without consent) | Hand off (T2) to the fraud queue, with the intake note |
| **Scam in progress** (someone is being talked into sending money right now, a "safe account", remote access, gift cards, crypto) | Hand off with **T7**, urgent, to the fraud queue |
| **Scam check question** ("is this text really from you?") | May answer, only from the scam awareness article |
| Credit report dispute | Hand off (T1) |
| Hardship or struggling to pay | Hand off (T3) |
| Fees and interest | May answer |
| Payments, deposits and withdrawals | May answer |
| Card and account features (rewards, statements, using the card, freezing it) | May answer |
| Opening or closing an account | May answer if customer initiated. Hand off if the bank closed it |
| Credit decisions (denials, limits) | Hand off (T1) |
| Unclear | Hand off (T1) |

**Flags:** legal or regulator mention, vulnerable customer, crisis language, third party acting for the holder, **account takeover signals** (locked out, details changed without permission), **suspected social engineering** (fake staff, requests to skip verification, asking whether an account exists), sensitive data shared, not English, attachment, abusive, instructions aimed at the bot.

### What happens, per case

| Case | Reply to the customer | Private note | Status | Label |
|---|---|---|---|---|
| Any must hand off category or flag | Fixed template (T1 to T3) | Category, flags, trigger, reason | pending to **open** | `handed-off` + category |
| Fraud already happened | T2 | **Fraud intake note** | pending to **open** | `handed-off`, `fraud` + category |
| Scam in progress, or account takeover signals | **T7** | Fraud intake note | pending to **open**, **priority high** | `handed-off`, `fraud-urgent`, `urgent` |
| Crisis language | **T4** | Reason | pending to **open**, **priority high** | `handed-off`, `urgent` |
| Suspected social engineering | T1. Never confirms whether an account exists | Reason | pending to **open** | `handed-off` |
| May answer, and help articles support it | **Cited answer** (the only model written text) + footer | Citations used | stays pending | `bot-answered` + category |
| May answer, but nothing supports it | T1 | "No supporting article" | **open** | `handed-off` |
| May answer, but key details missing | T5 listing exactly what's missing | Missing fields | stays pending | `needs-info` |
| Sensitive number in the message | Adds T6 to whichever reply goes out | "Sensitive data masked" | as above | as above |
| Customer writes again after any Warmhand reply | None | "Customer follow up" | **open** | `handed-off` |
| Any error | T1 if Chatwoot is reachable | Error type | **open** | `handed-off` |

**Allowed labels, fixed set:** the twelve category labels, plus `bot-answered`, `needs-info`, `handed-off`, `fraud`, `fraud-urgent`, `urgent`.

### The rules

**Code** is a hard check before any Chatwoot write, holding even if the model is fully manipulated. **Prompt** is an instruction. Prompt rules are wishes, code rules are guarantees.

| # | Rule | Enforced by |
|---|---|---|
| 1 | Warmhand can only **post one message, add a private note, add a label from the fixed set, move the status from pending to open, and set priority to high on urgent cases.** It never resolves, deletes, edits contacts, assigns named people, or touches another conversation | Code allowlist. The bot token may allow more, so our code is the wall |
| 2 | Legal clock and fraud cases get a **fixed template**, never generated text (policy section 1) | Code forces the template |
| 3 | **No commitments, no advice:** no refunds, credits, reversals, waivers or timelines promised, no liability statements, no legal, tax or investment advice, no credit decisions | Prompt, plus an outgoing text scan for promise phrases, plus gold set cases |
| 4 | Every factual claim in an answer is backed by a retrieved help article passage. **Each citation carries the article, the chunk ID and a short verbatim quote, and code checks the quote really appears in that chunk.** If no citation survives the check, Warmhand hands off. **Links only go to the Kettlewick help center** | Code: citation must be in the retrieved set and its quote (8+ characters, whitespace normalized) must match the chunk text. Link domain check. Evals check the quote supports the claim |
| 5 | **Vulnerable customers and crisis language** get the care or crisis template and a human, immediately | Keyword net in code plus the model. Either triggers |
| 6 | Acts only on **incoming customer messages in the configured inbox** | Code |
| 7 | **At most one Warmhand message per conversation.** A repeated webhook never double posts. Before posting, it rechecks for newer customer messages and hands off if any exist. Any later customer message means a handoff | Code, keyed on message and conversation IDs |
| 8 | **Message text is data, never instructions.** Injection attempts hand off | Code limits (rules 1, 2, 4, 9) plus the prompt plus gold set cases |
| 9 | **Never asks for or repeats sensitive data.** Outgoing text is scanned for card number patterns and words like PIN, CVV, passcode, password, one time code, SSN, and blocked with T1 as the fallback | Code |

### Operations

- **Autonomy ladder.** Autonomy is earned one rung at a time:

| Rung | What Warmhand does | Promotion to the next rung |
|---|---|---|
| 0: Shadow (default) | Posts nothing public. Every conversation is handed off, with the would-be reply in a private note | All gold set gates pass, and 20 live shadow conversations are reviewed with zero wrong would-be replies |
| 1: Live, full review | Sends templates and cited answers live. **A human reviews every bot answer** within a day | Two weeks or 50 answers with zero wrong answers in review, and the nightly gate green |
| 2: Sampled review | A human reviews a random 20% of answers | V1, earned by rung 1 |
| 3: Multi turn | Answers follow ups in "may answer" categories | V1, earned by rung 2 |

Handoffs, fraud routing and the watchdog work the same on every rung. Only what the *customer* sees changes
- **Watchdog:** any conversation still pending with no Warmhand action after 5 minutes is moved to open with a note. No customer is ever stuck in the bot's queue
- **Kill switch:** remove the agent bot from the inbox in Chatwoot settings. No deploy needed
- **Decision log:** conversation and message IDs, category, flags, trigger, action, citations, model and prompt version, latency, cost. **Never** names, emails, phone numbers or message text. Retention: 30 days
- **Configurable per tenant:** bank name, help center URL, label names, watchdog timeout, shadow mode on or off

### Test environment

Chatwoot Cloud trial account, one inbox, the Warmhand agent bot, a `fraud` team or queue. The Kettlewick help page from Lovable with the widget. A gold set built from CFPB complaints.

**The ten help articles (proposed):** outlined by Subhasish, drafted by Claude, edited by Subhasish.
1. Fees at Kettlewick (monthly, overdraft, foreign transaction, late payment)
2. How interest works on your credit card
3. Statements and payment due dates
4. Freezing or replacing your card
5. Rewards: earning and redeeming
6. Deposits, withdrawals and ATM limits
7. Closing your account
8. **Spotting scams: what Kettlewick will never ask you**
9. **You see a charge you don't recognize: what to do right now**
10. Talking to a person: how to reach our team (the anti doom loop article)

### MVP flows and user stories

Six flows, 22 user stories, each with Given, When, Then acceptance criteria, and a traceability table showing every hard gate has at least one story: `docs/flows_and_stories.md`.

| Flow | Stories | Phase |
|---|---|---|
| 1. A question the help articles answer | US-1 to US-3 | A |
| 2. The customer needs a human (legal clock, people, channel safety, follow ups) | US-4 to US-8 | A |
| 3. A scam in progress, or fraud already happened | US-9 to US-13 | A (US-13 in B) |
| 4. Channel safety and failure | US-14 to US-17 | A |
| 5. The operator keeps it safe | US-18 to US-21 | A (US-21 in B) |
| 6. An evaluator re-runs the test set | US-22 | B |

## 7. Success metrics

### Hard gates, on the gold set

**The gold set:** about 60 cases. About 40 are real CFPB complaints across all categories, rewritten as short chat messages (raw data stays in `data/raw/`, never committed, never quoted). About 20 are adversarial: injection, card numbers in the message, third party requests, crisis language, legal threats, duplicate webhooks, message bursts, and **8 fraud cases** (scam in progress x3, account takeover x1, social engineering x2, scam check questions x2). **Labels:** Subhasish labels every case, Claude labels independently, and every disagreement is reviewed and recorded before the first run. Every case has an expected category, flags, action and, for answerable ones, the expected answer, all **written before the first run**. Phase A uses about 20 cases run by hand.

| Gate | Target |
|---|---|
| Wrong answers (any claim unsupported by its citation, or contradicting the expected answer) | 0 |
| Must hand off cases handed off (legal clock, people, channel safety) | 100% |
| Replies asking for or repeating sensitive data | 0 |
| Replies containing a commitment or advice | 0 |
| Unmasked card or account numbers in logs or model inputs | 0 |
| Duplicate replies under replayed webhooks | 0 |
| Writes outside the allowlist | 0 |
| Conversations left pending past the watchdog limit | 0 |
| Fraud cases routed to the fraud queue | 100% |
| Scam in progress cases that get T7 and urgent priority | 100% |
| Fraud replies that reassure about liability or refunds ("you won't lose anything") | 0 |

**Honest limit:** 0 wrong out of 60 means the true rate is likely under about 5%, not zero. The gate is necessary, not sufficient.

### Tracked, no target in V0

| Metric | Definition |
|---|---|
| Answer rate | Share of messages Warmhand answered. Expected to be low on complaint data |
| Category accuracy | Against CFPB derived labels |
| Time to first response | Message received to Warmhand's reply, under 60 seconds for 95% |
| Cost per conversation | Ceiling set after the first real API call |
| Fraud note accuracy | Intake fields against gold labels. "Unknown" is correct when the message doesn't say |
| Keyword only handoffs | Handoffs triggered by the keyword net alone, to spot false positives |
| Fraud false positives | Messages flagged as fraud that weren't |

## 8. Release

| Phase | Scope | Budget | Proof |
|---|---|---|---|
| **A: Demo** | Modules 1 to 6: API, structured output and masking, tools and the allowlist, the graph, retrieval over the help articles, the live Chatwoot bot with shadow mode | About 17 to 19 hours | Builder goal 1 |
| **B: Production** | Modules 7 to 10: MCP, deployment, nightly gate, checker agent experiment, red team, release memo | After Phase A | Builder goal 2 |
| **C: Packaging** | Module 11: README, recording, diagram, eval results page | After Phase B | Builder goal 3 |

**Beyond V0:** V1 adds multi turn answers for "may answer" categories and auto-resolving silent answered conversations, earned by two weeks of zero wrong answers. V2 is a helpdesk marketplace listing, earned by a real support team asking to try it.

## 9. Assumptions

| Assumption | Status | Checked in |
|---|---|---|
| Agent bots, webhooks and the API work on Chatwoot Cloud's Startups plan and trial | To verify | Stage 4, inside the trial |
| The bot token can post, add notes, add labels and change status | To verify | Stage 4 |
| Webhook authenticity can be verified (there's an open signature bug for account webhooks) | To verify | Stage 4 |
| Enough CFPB complaints carry narratives to build 40 realistic cases | To verify | Stage 4 |
| CFPB complaints are a proxy for chat messages, skewed toward severe cases | **Accepted limit** | n/a |
| US rules are the right frame for a fictional US bank | Accepted | n/a |
| English only | Accepted limit | n/a |
| Model cost allows a nightly 60 case run | To verify | Module 1 |
| Chatwoot labels, teams and priority can drive a separate fraud queue | To verify | Stage 4 |
| Chatwoot Startups plan costs $19 per agent per month, one agent, for the build months | Accepted cost | n/a |

## 10. Risks and mitigations

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Wrong information about disputes or deadlines misleads a customer | High | Medium | Legal clock cases never get generated text (rule 2). Answers only from cited articles (rule 4) |
| Bot behavior looks like phishing | High | Low | Rule 9 in code, T6 line |
| A vulnerable customer gets an automated answer | High | Medium | Keyword net plus model, either triggers (rule 5). Crisis template reviewed |
| Personal data reaches the model provider or logs | High | Medium | Masking before the model and the log. A zero gate |
| Prompt injection | High | Medium | Rules 1, 2, 4, 9 in code. Adversarial gold set cases |
| Conversation stuck in the bot's queue | High | Medium | Fail by handing off, plus the watchdog |
| Too close to the builder's former employer | High | Low | Fictional bank, no student loans, no employer flows or policies. Written into project instructions |
| Mistaken for a real bank | Medium | Low | Name checked for collisions, "fictional bank, demo only" on every page and message |
| Chatwoot changes plans again (the free plan already lost API access) | Medium | Medium | Thin adapter around Chatwoot, so the helpdesk can be swapped |
| CFPB data availability changes | Medium | Low | The gold set is a committed snapshot |
| Fraud false positives flood the fraud queue | Medium | Medium | Tracked metric. Accepted at launch, since a missed scam costs far more than a false alarm |
| A scam victim gets a cheerful answer | High | Medium | Scam in progress is a hand off category with a fixed template, two nets, and a 100% gate |
| Phase A overruns | High | High | Phase A is the only commitment. Help articles capped at about 10 |
| A model or vendor is retired | Medium | Medium | Model name in config, swap and rerun the gate |
| Chatwoot Captain or Fin makes Warmhand redundant for any real bank | High | Already true | Position as a reference agent plus open benchmark, not a product. The README says plainly: a real bank should start with its helpdesk's AI |

## 11. Open questions

| # | Question | Owner | Blocking? |
|---|---|---|---|
| 1 | Approve the ten proposed help article topics (section 6) | Subhasish | Blocks Module 5 |
| 2 | Watchdog timeout: is 5 minutes right? | Subhasish | No |
| 3 | Crisis template wording review | Subhasish | Before any live demo |
| 4 | Log retention: is 30 days right? | Subhasish | No |

## 12. Competitive landscape

Full brief with the battlecard vs Fin: `docs/competitive_brief.md`. Researched 21st September 2026.

| # | Competitor | What they do | Same feature test |
|---|---|---|---|
| 1 | Chatwoot Captain | AI agent inside the same helpdesk, learns from the help center, hands off | **Fails.** Anything Warmhand adds, Chatwoot can add |
| 2 | Intercom Fin | Market leader. $0.99 per outcome, "Procedures" with deterministic controls, audit trails, claims about 0.1% hallucination | Code guardrails **fail**. **Survives:** Fin publishes rates, not its test set |
| 3 | Zendesk AI agents | Paid per automated resolution | **Survives as counter positioning:** paid per answer, so it won't sell escalation |
| 4 | Decagon | Layered guardrails, regression tests, escalation rules | Fails. Same shape, which validates the design |
| 5 | Sierra | Enterprise, about $150k a year (third party) | Fails. Different buyer |
| 6 | Salesforce Agentforce | $2 per conversation (third party) | Fails. Different buyer |
| 7 | Kasisto (Backbase) | Banking specialist, multiple agents, compliance positioning | Fails, positioning only |
| 8 | Posh | Credit unions, headline "containment up to 99%" | **Survives as counter positioning:** Warmhand measures correct handoffs, not containment |
| 9 | interface.ai | Agentic AI for credit unions, including collections | Never moving money is a deliberate limit, not a moat |
| 10 | In house (e.g. Bank of America's Erica) | Built by the largest banks | Different league |

**What survives:** one thing. **An open, reproducible handoff benchmark** built from public CFPB complaints, with the policy mapping and results published. Vendors publish claims, not test sets, and a published results history can only be earned.

**Positioning:** for people deploying or evaluating AI support in regulated finance, Warmhand is an open reference agent and handoff benchmark that shows, on real public complaint data, which conversations a bank bot must never own and whether it hands them off, because the policy, test set and results are published and reproducible.

**Mapped to the CFPB's chatbot concerns (goes in the README):**

| CFPB concern | Warmhand's answer |
|---|---|
| Wrong answers | Cited answers only, citations checked in code, zero wrong answers gate |
| Failing to recognize disputes unless the right words are used | Keyword floor in code plus the model reading for meaning. Either one hands off. 100% recall gate |
| Doom loops | One bot reply, then a human. A watchdog within 5 minutes |
| Privacy and phishing | Masking before the model and the logs. Code blocks any request for sensitive data |
| (Beyond the CFPB list) fraud victims mid-scam | Scam in progress interrupt, fraud queue, structured intake note |

**Consequences (no new scope):**
- The gold set, policy mapping and results are packaged so a stranger can re-run them against any bot. That's the benchmark. It was already planned; now it's the headline
- New key result: the benchmark is published in the repo in a re-runnable form
- The README says plainly: a real bank should start with its helpdesk's built in AI
- Never claim Warmhand is compliant, or better than any vendor

## 13. Deferred sections

| Section | Where | Why not now |
|---|---|---|
| Technical approach and feasibility | Stage 4 | Needs the Chatwoot and CFPB checks |
| Pricing, distribution | Modules 11 and 12 | Pricing before the first API call is fiction |
