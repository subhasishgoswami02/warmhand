# Current state

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

Consequence: the gold set splits in two. Escalation cases come from the archived narratives (June, July and August 2026 exports, which overlap the current structured data window by about seven weeks). Answerable cases are written by hand from the help articles, because a regulator complaint corpus contains almost no easy questions by construction. Current structured data sets the category weights and provides a cross-check. Full detail and caveats: `data/SOURCE.md`.

This also strengthens the positioning. The supply of real, public, categorized bank complaint text is now finite and cannot be regenerated by anyone.

PRD corrections pending: the evidence section cites live narratives, the risk "a data source disappears" moves from hypothetical to realized with a date, and the gold set section splits into two halves with the PII masker carved out (archived narratives are pre-redacted, so they cannot test masking).

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
