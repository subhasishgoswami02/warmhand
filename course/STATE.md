# Current state

## AUDIT, 28th September 2026: the project had drifted

Measured: 39,636 words of markdown, 347 lines of Python (all data wrangling), **zero calls to a language model**, 11 commits, 10 days. The stated goal was hands-on experience with agentic systems. Nothing in the repo was an agent.

Diagnosis: every "carry on" produced another document, because documents are the fastest thing to produce and they feel like progress. Scope grew rather than shrank, against the project's own rule.

Also named: the evaluation is **circular**. The policy author is the label author, the bank is fictional and the help articles are invented, so a perfect score measures compliance with the policy, not the quality of the policy. This is now stated in the README rather than discovered by a reviewer.

Actions taken the same day:
1. Gold set cut from 120 real cases to **30**, so the loop closes in one sitting
2. `course/MODULE_01.md` written: the first API call, about 30 lines, typed by Subhasish. **Nothing else is added to this repo until it runs**
3. `README.md` written, with a Limitations section that names the circularity, the post-failure corpus, the length mismatch, and the fact that nobody asked for this test set
4. `evals/SECOND_LABELLER.md`: a brief for one person with bank operations experience to label 10 cases blind. The agreement rate gets published whatever it is
5. Feature work frozen: fraud extensions, the audit log, Chatwoot and the recipes folder all wait

Open, unbudgeted: there is no cost per complaint, because no API call has been made. Module 1 produces that number and it goes in this file.


**Read this before doing anything.** Both Claude Code and the Cowork project chat should update it when something changes. If this file disagrees with HANDOFF.md, this file wins.

Last updated: 24th September 2026. Stage 3 done, PRD v1.4, Module 0B done and the repo is public. See docs/pivot_change_map.md.

## Repo

Lives at `~/Developer/triage-agent`. It was moved here from `~/Documents/triage-agent`, so any doc still saying Documents is stale.

**Public at https://github.com/subhasishgoswami02/warmhand**, MIT licensed, pushed 24th September 2026.

**History note.** The first commit was originally `fd0cb78`. It was amended to `58ef2f1` before the first push, to strip career sensitive lines (a named prospective employer, a former employer) from `course/HANDOFF.md` and `course/PROJECT_INSTRUCTIONS.md`. Safe to do because nothing had been pushed and no remote existed. `fd0cb78` is still in the local reflog, unreachable, and was never pushed. Any doc citing `fd0cb78` is stale.

## Module 0: complete

All four proofs passed:
- venv created at `.venv`, and `which python` resolves to `.venv/bin/python`
- prompt shows `(.venv)` when activated
- `git init`, one commit `58ef2f1` "Module 0: repo skeleton, secret hygiene, course plan"
- `.env` created from `.env.example` and correctly ignored. `git status` does not list it

Optional tidy-up, not blocking: `python -m pip install --upgrade pip` with the venv active.

**Explain-back: passed, 24th September 2026.** All four answered in his own words.

- Committed key: correct, including that rotation is the only real fix. Sharpened: the old commit is directly viewable, no rollback needed, and bots scrape public repos within seconds
- `--amend`: correct on why it was safe pre-push. Sharpened: after a push, rewriting is cosmetic because the content is already on GitHub's servers, in caches and in clones
- `.env.example` vs `.env`: half on first pass. Corrected: the example is the shopping list of variable names so a cloner knows what to supply, and `.gitignore`, not the example file, is what keeps the real `.env` out
- Hook vs `.gitignore`: correct, including the `git add -f` case. Added: `.gitignore` also does nothing for a file that is already tracked

## Module 0B: complete, 24th September 2026

**Public at https://github.com/subhasishgoswami02/warmhand**, MIT licensed, pushed 24th September 2026.

Five commits on `main`, all pushed:

| Commit | What |
|---|---|
| `58ef2f1` | Module 0: repo skeleton, secret hygiene, course plan (amended, see the history note below) |
| `68fd73d` | Archive GitHub-era PRD and competitive brief |
| `72bfb9d` | MIT license and a pre-commit hook that blocks `.env` files |
| `ea33a7b` | Pivot to bank complaint triage: Warmhand PRD v1.4, escalation policy, flows and stories |
| `c4943f0` | Module 0B: the hook needs `core.hooksPath` after every clone |

**History note.** The first commit was originally `fd0cb78`. It was amended to `58ef2f1` before the first push, to strip career sensitive lines (a named prospective employer, a former employer) from `course/HANDOFF.md` and `course/PROJECT_INSTRUCTIONS.md`. Safe because nothing had been pushed and no remote existed. `fd0cb78` is still in the local reflog, unreachable, and was never pushed. Any doc citing `fd0cb78` is stale.

**The rule that came out of it:** for a public repo, scan history (`git grep` across `git rev-list --all`), not just the working tree. A working tree scan misses everything already committed. This nearly shipped the interview details publicly.

Proofs passed: the hook refused a staged fake `.env`; every commit scanned clean for secrets and career sensitive terms; GitHub contents match local; no `.env`, `references/`, `data/raw/` or `traces/` on the remote.

**GitHub push protection: on.** Confirmed 24th September 2026 under Settings, Security and quality, Advanced Security. Secret Protection and Push protection were both already enabled.

## PIVOT, 19th September 2026: GitHub issue triage is dropped, bank complaint triage replaces it

**Read `docs/pivot_change_map.md` before doing anything.** It lists every change (46 items) and the execution order.

Why: Stage 2 showed GitHub issue triage is being absorbed by the platform (GitHub Agentic Workflows ships code enforced write limits) and Dosu left the category in August 2026. The new domain: Warmhand triages customer complaints for a **fictional digital bank**. It uses the public CFPB complaint database for evals (real, categorized complaints), Chatwoot (open source helpdesk) as the live system, and the escalation matrix as a compliance policy.

What is superseded: everything GitHub specific in `prd.md` v0.3, `course/SYLLABUS.md`, `course/HANDOFF.md`, `course/PROJECT_INSTRUCTIONS.md`. The GitHub era brief is archived at `docs/archive/github/`. Not yet rewritten, pending the decisions below.

Hard boundary added: no student loans, no former employer flows or policies as templates, fictional bank only, never quote an individual CFPB narrative.

Done in the pivot so far: `course/SYLLABUS.md` v2 (the full learning map, Part 0 to after launch), `.env.example` (Chatwoot variables replace GitHub), `.gitignore` (`data/raw/`), GitHub brief archived, change map written.

**Found, needs Claude Code before the next commit:** the repo has **no remote and no LICENSE**. Hard constraint 3 (public, MIT, from commit one) is not met yet.

**Pre PRD checks, 20th September (see `docs/research/2026-09-20_pre_prd_checks.md`):**
- "FirstPass" is already a real bank's voice biometrics login (First Financial Bank). Rename recommended: Warmhand (from "warm handoff"). Bank name candidate: Brindlecove Bank
- Chatwoot Cloud's free plan lost API and webhooks on 16th July 2026. Recommended: Startups plan ($19 per agent per month) via the 15 day trial first. Self hosting is the alternative
- CFPB data: under the draft mapping, about 56% of credit card complaints (98,125 in the last year) are must escalate categories. For checking and savings, at least 16%
- HANDOFF.md and PROJECT_INSTRUCTIONS.md updated for the new domain. Subhasish still needs to paste the instructions into claude.ai

**Decided 20th September:**
- **Names:** agent **Warmhand** (from "warm handoff"), fictional bank **Kettlewick Bank**. He wanted a Harry Potter theme. Franchise names are trademarked, so the bank keeps the flavor and the agent name carries the positioning
- Chatwoot Cloud Startups plan, starting with the 15 day free trial
- Scope: credit cards plus checking and savings accounts only
- Help articles: Subhasish outlines, Claude drafts, Subhasish edits
- The brain dump was drafted by Claude at his request (general industry knowledge only). He reviews and edits it

**Written 20th September, awaiting his review:** `prd.md` v1.0 (Warmhand), `docs/escalation_policy.md` v0.1, the pivot section of `brain_dump.md`. The GitHub era PRD is archived at `docs/archive/github/prd_v0.3.md`.

**Stage 2 redo done, 21st September:** `docs/competitive_brief.md` (bank support agents), PRD v1.1. Finding: Chatwoot Captain (same helpdesk) and Intercom Fin (Procedures, audit trails, a claimed 0.1% hallucination rate) already cover guardrails in code. The only thing that survives the same feature test is **an open, reproducible handoff benchmark** built from public CFPB data, with the policy mapping and results published. Positioning: an open reference agent and handoff benchmark, mapped to the CFPB's June 2023 chatbot concerns (wrong answers, missed disputes, doom loops, privacy). Battlecard vs Fin ready for interviews.

**22nd September:** decided to build first. The Captain comparison is optional, for later. Six apps from Shubham Saboo's awesome-llm-apps (Apache 2.0, commit c622878) are copied into `references/awesome-llm-apps/`, which is **gitignored** (someone else's code, read only, never in Warmhand's history). Review: `docs/research/2026-09-22_reference_code_review.md`. Adopted: verbatim quote citations checked in code (PRD rule 4), a relevance gate before the model, tests with a fake model, Corrective RAG as the Module 4 reference graph, an optional hash chained log in Module 8. PRD is now v1.2. Decided: the recipes folder (every module's proof packaged as a runnable recipe) and a pull request to awesome-llm-apps in Phase C.

**Fraud added, 22nd September:** Warmhand detects fraud signals in the conversation (no transaction data). A scam in progress or account takeover gets fixed template T7, urgent priority and the fraud queue. Fraud handoffs carry a structured intake note. Scam check questions may be answered from the scam awareness article. Social engineering aimed at the bot is handed off. Transaction monitoring stays out of scope. Design: `docs/research/2026-09-22_fraud_angle.md`. Policy v0.2 adds section 3A and T7.

**PRD review round 1:** `docs/reviews/2026-09-22_prd_v1.2_review.md`. Fixed in v1.3: classification now always runs (v1.2's relevance gate could skip the model on crisis or scam messages), priority routing, human review of every bot answer early on, an autonomy ladder, proposed help article topics. The only open P0 is user stories (Stage 3).

**Module 0B written:** `course/MODULE_00B.md`, step by step: the `.env` pre-commit hook, the MIT license, three commits, the public repo `warmhand`, GitHub push protection, and the four explain back questions.

**Stage 3 done, 22nd September:** `docs/flows_and_stories.md`. Six flows, 22 user stories (US-1 to US-22), Given/When/Then acceptance criteria, a pipeline diagram, gate traceability, and a list of what was cut on purpose. PRD v1.4. The review's last P0 (no user stories) is closed.

**Data source change found, 24th September 2026.** The CFPB stopped publishing consumer complaint narratives on 14th August 2026, six weeks before we looked. Verified three ways (website export, full database download, public API): the published data now has 15 columns and no narrative field. Narratives published before that date were not withdrawn; the CFPB moved them to its FOIA Electronic Reading Room as direct bulk downloads covering December 2011 to 14th August 2026.

Consequence: the gold set splits in two. Escalation cases come from the archived narratives. Five monthly exports downloaded, April to August 2026: 23,416 credit card and checking complaints with text. April to June is the primary pool, July supplementary, August has none (publication stopped on the 14th). Answerable cases are written by hand from the help articles, because a regulator complaint corpus contains almost no easy questions by construction. Current structured data sets the category weights and provides a cross-check. Full detail and caveats: `data/SOURCE.md`.

This also strengthens the positioning. The supply of real, public, categorized bank complaint text is now finite and cannot be regenerated by anyone.

PRD corrections pending: the evidence section cites live narratives, the risk "a data source disappears" moves from hypothetical to realized with a date, and the gold set section splits into two halves with the PII masker carved out (archived narratives are pre-redacted, so they cannot test masking).

**Gold set pool measured, 27th September 2026.** `scripts/count_strata.py` (first code in the repo). Primary pool April to June 2026: 19,569 complaints with narrative text across credit card and checking or savings. Every stratum is comfortably supplied, so **July is excluded** and the publication-cutoff selection bias leaves the sample entirely. Reg Z 3,351, Reg E 1,659, Older American 1,590, Servicemember 1,774.

Cross-check passed: filtering the current structured export in code reproduces 42,847 / 21,693 / 21,154 exactly, matching the website's own export.

New finding: median narrative is 206 words (90th percentile 478, max 5,347). These are written submissions, not chat turns. Decision recorded in `data/SOURCE.md`: the full narrative is the input, and the README says so rather than implying the agent was tested on short chat messages.

**Gold set drawn, 27th September 2026.** `scripts/build_gold_set.py`, seed 20260927, reproducible. 120 cases in `evals/gold_set_raw.csv` (gitignored, holds narrative text). Disjoint strata by priority so nothing appears twice: Reg Z 25, Reg E 25, Older American 20, Servicemember 20, ambiguous middle 30. Drawn from April to June 2026 only.

Sanity check on the draw: median 204 words, longest 814, and 17 of 120 are over 400 words, which is close to the 10 to 15 percent the full pool predicted.

Policy v0.3 adds two length triggers in section 3 (hand off over 400 words, truncate the model's view at 2,000) with the measured basis recorded. Stories US-23 and US-24 added, including the adversarial case: an injection buried at word 2,500 of a 3,000 word complaint.

`evals/LABELLING.md` has the labelling instructions. **Next human step: Subhasish labels all 120.** Two to three hours, two sittings. No model labels any of them, or the benchmark measures nothing. Label on content and ignore the length rule while labelling, so the two rules can be compared rather than one baked into the other.

**Help articles written, 27th September 2026.** `docs/help_articles/`, five articles, about 2,000 words. Cut from the PRD's proposed ten using the measured issue counts: fees, statements and interest, cards, spotting scams, reaching a person. The folder README records every cut with its reason, so nothing gets reinvented later.

Two rules enforced inside the articles: every sentence states a number or states nothing (a vague sentence produces an unverifiable citation), and no sentence promises an outcome, quotes a legal deadline or states entitlement. Each article ends with what it does not cover, which is what the relevance gate should refuse.

PRD open question 1 (approve help article topics, was blocking Module 5) is closed. Subhasish reviews and edits the wording; the fee numbers are invented and his to change.

**Synthetic half written, 27th September 2026.** `evals/synthetic_cases.csv`, 40 cases against the five articles: 25 genuinely answerable, 15 near misses that look answerable and are not (a legal deadline dressed as a policy question, an account-specific question dressed as a fees question, bereavement inside a how-to, SCRA inside a rates question, a scam in progress, a direct injection). Committable, since it contains no CFPB text.

Its `proposed_decision` column is Claude's and is a draft, not a label. Subhasish overrules it in the same three columns as the real cases. Cases where he overrules are kept visible on purpose.

Gold set now stands at 160: 120 real complaints (April to June, stratified, seed 20260927) plus these 40.

**Reproducibility and masker tests written, 28th September 2026.**

`evals/rehydrate.py`: rebuilds the gold set's complaint text from IDs. Important correction to the earlier plan: the live CFPB API cannot do this, because the Bureau stopped publishing narratives on 14th August 2026. Rehydration reads the archived monthly exports instead, and downloads them if missing. Missing IDs (consumer withdrew consent) are reported, never silently dropped.

`scripts/split_gold_set.py`: turns the labelled file into the committable one, dropping narrative text. Refuses to write if any case is unlabelled, so a half finished pass cannot be published as complete.

`evals/pii/`: 22 recall cases and 18 precision cases for the PII masker, plus a README. Synthetic on purpose: CFPB narratives arrive pre-redacted, so they would score a masker at 100 percent and prove nothing. Card numbers are the published processor test numbers, SSNs use the never-issued 999 prefix, the routing number is checksum valid and unassigned. Nothing belongs to anybody, so the set is publishable.

Two decisions left open on purpose in `evals/pii/README.md`: whether a 16 digit number failing the Luhn check should still be masked, and how to treat digits that are an amount in one reading and an identifier in another. Both need a recorded decision, not a default.

**Next:** Stage 4 technical discovery, run as hands-on spikes rather than another document. Spike 1 (blocking): CFPB narrative availability, does the public API actually return consumer written complaint text and how much of it. Spike 2: model cost and latency on one real complaint. Deferred until needed, around Module 6: the Chatwoot trial checks (agent bots, API, labels, teams, priority, webhook signature) and a tunnel for local webhooks, because the trial clock starts at signup. Then Module 1, the first API call against a real CFPB complaint. Still open for his review: PRD v1.4, escalation policy v0.2, `docs/flows_and_stories.md`, the help article list (10 proposed, recommend cutting to 5), crisis template wording, watchdog timeout, log retention.

Commit order, so the pivot shows in history (this replaces the earlier order):
1. `docs/archive/github/` (the GitHub era PRD and brief, as evidence)
2. LICENSE (MIT), then create the public GitHub repo and push
3. The pivot: everything else

Tool decisions: LangGraph core. Checker agent experiment in Phase B, kept only if evals show fewer wrong answers at acceptable cost. Claude Code hook to block `.env` commits. Lovable in Phase A (fictional bank help page hosting the Chatwoot widget) and Phase C (eval results page). Fin benchmark optional later. Not used: Obsidian, Graphify, n8n, Replit, Hermes Agent.

Goal: quality plus credibility. Ship from scratch to production, never wrong in public, and prove it.

## Next after both

Module 1: the first real API call. Auth headers, tokens, latency, cost, error codes, retries with backoff.

## Division of work

| Where | Owns |
|---|---|
| Claude Code, terminal | Modules 0 to 10. All code and commits |
| Cowork project "Triage Agent" | PRD, content, packaging, monetisation |
| Separate Cowork chat | Interview prep. Not part of this repo |
