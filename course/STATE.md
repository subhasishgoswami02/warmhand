# Current state

**Read this before doing anything.** Both Claude Code and the Cowork project chat should update it when something changes. If this file disagrees with HANDOFF.md, this file wins.

Last updated: 22nd September 2026. Stage 3 done, PRD v1.4. See docs/pivot_change_map.md.

## Repo

Lives at `~/Developer/triage-agent`. It was moved here from `~/Documents/triage-agent`, so any doc still saying Documents is stale.

## Module 0: complete

All four proofs passed:
- venv created at `.venv`, and `which python` resolves to `.venv/bin/python`
- prompt shows `(.venv)` when activated
- `git init`, one commit `58ef2f1` "Module 0: repo skeleton, secret hygiene, course plan"
- `.env` created from `.env.example` and correctly ignored. `git status` does not list it

Optional tidy-up, not blocking: `python -m pip install --upgrade pip` with the venv active.

**Pending, the explain-back. Subhasish answers these in his own words. Do not accept "it worked" as understanding, and do not answer them for him:**

1. What does a virtual environment protect you from?
2. Why is `.env.example` committed but `.env` is not?
3. If you commit an API key and delete it in the very next commit, is the key safe?

Question 3 is the one people get wrong. The answer is no, and the reason matters.

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

**Next:** Subhasish reviews the flows and stories, runs Module 0B in Claude Code, then Stage 4 (technical discovery: the Chatwoot trial checks and the CFPB narrative checks). Then Stage 3 (flows, user stories, acceptance criteria), then Stage 4 (Chatwoot trial and CFPB checks). In parallel in Claude Code: the Module 0 gaps (LICENSE, public repo, `.env` hook), the Module 0 explain back, then Module 1.

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
