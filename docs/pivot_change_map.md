# Pivot change map: GitHub issue triage to bank complaint triage

**Decided:** 19th September 2026, by Subhasish.
**Why:** Stage 2 showed GitHub issue triage is being absorbed by the platform (GitHub Agentic Workflows) and the best known player (Dosu) left the category. Bank complaint triage is a live market, escalation errors there cost money and carry regulatory weight, real labeled public data exists (CFPB complaint database), and it is where the builder has 14 years of domain judgment.

**Method:** two passes. Pass 1 walks every artifact from the first file to the last. Pass 2 traces one customer message through the running system, then the build from Module 0 to launch, and lists only what pass 1 missed.

---

## What does not change

| Item | Why it survives |
|---|---|
| Stack: Python, LangGraph, FastAPI, SQLite then Postgres, Anthropic API | Domain agnostic |
| Modules 0 to 5 concepts (API call, structured output, tools, graph, retrieval) | Domain agnostic. Only the example content changes |
| Modules 7 to 10 concepts (MCP, production, evals, red team) | Domain agnostic |
| Operating principle: precision over coverage | Matters even more in finance |
| Model free text in exactly one path, every other reply a fixed template | Same |
| Hard limits in code, not only in the prompt | Same |
| Idempotency, dry run, kill switch, fail closed, decision log without personal data | Same principles, new mechanics |
| Phases A, B, C and the demo cut (Modules 1 to 6) | Same |
| Builder goals, OKR (quality plus credibility) | Same |
| Rules of engagement: he types the code, proofs, explain back | Same |
| ~~Name FirstPass~~ | **Changed 20th Sept:** FirstPass is a real bank's voice biometrics login. The agent is now **Warmhand**, the fictional bank is **Kettlewick Bank** |
| Repo folder `~/Developer/triage-agent` | "Triage" still true |

---

## Pass 1: every artifact, start to end

| # | Artifact | What changes | Who | When |
|---|---|---|---|---|
| 1 | Claude Project custom instructions (claude.ai settings) | "GitHub issue triage agent" becomes "bank complaint triage agent". Hard constraint 1 becomes "public data (CFPB) and synthetic cases only, no student loans, fictional bank only". Monetisation: "GitHub Marketplace app" becomes "helpdesk app marketplace" | Subhasish pastes, Claude drafts | After PRD v1.0 |
| 2 | Claude Project description | "Production GitHub issue triage agent" becomes "Production bank complaint triage agent" | Subhasish | Same time |
| 3 | `course/PROJECT_INSTRUCTIONS.md` (source of truth for 1) (DONE 20th Sept) | Same edits as 1 | Claude | Same time |
| 4 | `course/HANDOFF.md` (DONE 20th Sept) | "What we are building", domain row in the locked decisions table, stale "where we are right now". Add a banner pointing to STATE.md | Claude | Same time |
| 5 | `course/SYLLABUS.md` (DONE 19th Sept, v2) | "What you will have". Module 5: retrieval over the fictional bank's help docs. Module 6: Chatwoot agent bot webhooks and API replace GitHub. Module 9: gold set from real CFPB complaints. Module 10: finance specific negative paths. Module 11: launch community (fintech and CX, not maintainers). Module 12: marketplace path. Content track titles for Modules 5, 6, 11 | Claude | Same time |
| 6 | `course/MODULE_00.md` | No change. Already done | none | n/a |
| 7 | `course/STATE.md` | Full update: pivot, decisions, next step | Claude | Now |
| 8 | `.env.example` | Remove `GITHUB_TOKEN`, `GITHUB_WEBHOOK_SECRET`. Add `CHATWOOT_BASE_URL`, `CHATWOOT_ACCOUNT_ID`, `CHATWOOT_BOT_TOKEN`, `CHATWOOT_INBOX_ID`, `WEBHOOK_SHARED_SECRET` | Claude edits, Subhasish commits | Now |
| 9 | Local `.env` | Same variable changes. Claude never reads this file | Subhasish | When Module 6 starts |
| 10 | `.gitignore` | Add `data/raw/` so bulk CFPB downloads are never committed. The small curated gold set stays committed | Claude | Now |
| 11 | `brain_dump.md` (DONE 20th Sept, pivot section drafted by Claude at his request) | Keep the original as history. Append a dated pivot section in his words, plus a new raw dump on regulated support from general industry knowledge (no former-employer specifics) | Subhasish writes, Claude files | Stage 1 redo |
| 12 | `prd.md` (DONE 20th Sept, v1.0) | Rewritten as v1.0 for the new domain. Every section changes: one line, descriptor, summary, why now, product goals, non goals, problem hypotheses, users, identity (Chatwoot agent bot, not GitHub App), events, categories, risk flags, action table, rules, operations, test environment, metrics, assumptions, risks, open questions, competitive section | Claude drafts, Subhasish reviews | Stage 1 redo |
| 13 | `docs/competitive_brief.md` (DONE 21st Sept, bank version) | Move to `docs/archive/github/` and keep. It is evidence of the pivot decision. New brief for fintech support agents (Fin, Zendesk, Decagon, Sierra, banking specific assistants, and Chatwoot's own AI agent, Captain) | Claude | Stage 2 redo |
| 14 | New `docs/escalation_policy.md` (DONE 20th Sept, v0.1 draft) | The finance escalation matrix as a standalone policy the code implements: disputes, unauthorized transactions, fraud, hardship, legal or regulator mentions, discrimination claims, vulnerable customer signals | Claude drafts, Subhasish signs off as policy owner | Stage 1 redo |
| 15 | README (not yet created) | Written for the new domain from the start. Must include "this is a fictional bank" and "not financial advice" | Claude, Module 11 | Later |
| 16 | Content track | First post changes: what CFPB complaint data says about where AI support must never answer. Second: the pivot itself (killing the first idea after the competitive analysis). Per module posts keep their concepts | Claude drafts, Subhasish publishes | After Stage 2 redo |
| 17 | Monetisation stance | Marketplace path moves from GitHub to helpdesk marketplaces. Consulting inbound becomes stronger (fintech support deployments). Ranking unchanged | Claude | With 1 |
| 18 | Tool decisions (from the tools review) | Record in STATE and SYLLABUS: checker agent experiment in Phase B, Claude Code hook blocking `.env` commits, Lovable in Phase A (see pass 2) and Phase C, Fin benchmark optional later. Obsidian, Graphify, n8n, Replit not used | Claude | Now |
| 19 | Claude Project knowledge (docs in the project) | Currently empty. Save PRD v1.0 and the escalation policy there once approved | Claude | After approval |

---

## Pass 2: trace the system end to end, only what pass 1 missed

### A. One customer message, from typing to logging

| # | Step | Found in pass 2 | Fix |
|---|---|---|---|
| 20 | Customer types in a chat widget | **The widget needs a web page to live on.** No fictional bank site exists | Lovable builds a one page fictional bank help site with the Chatwoot widget. Moves Lovable into **Phase A** |
| 21 | Chatwoot hosting | Free cloud plan (Hacker: 2 agents, 500 conversations a month, live chat only). Unverified whether agent bots work on it | Stage 4 check. Fallbacks: 15 day trial, or self host with Docker |
| 22 | Webhook reaches Warmhand | **Chatwoot's webhook signature has an open bug** (signature cannot be verified with the secret the API returns, opened 14th March 2026, applies to account webhooks) | Stage 4 check for agent bot webhooks. Fallback: shared secret in the URL plus a source check |
| 23 | Eligibility | New rules replace "ignore pull requests": act only on incoming customer messages in the one configured inbox. Ignore agent messages, private notes, other inboxes, and the bot's own messages | Rule 6 rewritten |
| 24 | Customer sends several messages quickly | **Race:** a second message arrives while Warmhand is drafting. Its reply would ignore it | Before posting, recheck for newer customer messages. If any, hand off instead |
| 25 | Personal data in the message | **Card numbers, account numbers, names, emails** will appear. They must not reach the model provider or the log unmasked | Mask them before the model call and before logging. New hard gate: zero unmasked personal data in logs |
| 26 | Classification | GitHub report types are gone. Categories follow the CFPB taxonomy for credit cards and bank accounts, cut down to a small set, so the gold set labels map one to one | Rewrite in PRD |
| 27 | Risk flags | New: unauthorized transaction or fraud, billing dispute, hardship, legal or regulator mention, discrimination claim, vulnerable customer signals, message not in English, attachment present | Every flag means hand off |
| 28 | Drafting a reply | **New rule: never ask for or repeat sensitive data** (full card number, CVV, PIN, one time codes, passwords, government ID). A bank bot asking for these is indistinguishable from phishing | New rule 9, enforced in code on outgoing text |
| 29 | Commitments | Rule 3 widens: no promising refunds, credits, fee waivers, reversals or timelines, no legal conclusions, no financial advice | Rule 3 rewritten |
| 30 | Handoff mechanics | Chatwoot hands off by moving the conversation from "pending" to "open". **A crash could leave a customer stuck in "pending", invisible to humans.** Failing silent was safe on GitHub, it is not safe here | Fail closed now means hand off. Plus a watchdog that opens any conversation left pending past a time limit |
| 31 | Explaining the escalation | **Chatwoot has private notes, visible to agents only.** This fixes the v0.2 gap where the reason lived only in a log | The reason goes in a private note on every handoff |
| 32 | Dry run | Better than before: in dry run, Warmhand writes its would-be reply as a private note, so a human sees exactly what it would have said. This is Linear's "suggest versus auto apply" | Shadow mode is the default until the live path is proven |
| 33 | Logging | Log conversation and message IDs, never contact name, email or phone | Same principle, new fields |

### B. The build, Module 0 to launch

| # | Where | Found in pass 2 | Fix |
|---|---|---|---|
| 34 | Hard constraint 3, "public repo from commit one" | **The repo has no remote and no LICENSE file.** Nothing is on GitHub yet | Before the next commit: add an MIT LICENSE, create the public GitHub repo, push |
| 35 | Git history | Four uncommitted files are GitHub era work. The pivot is only visible as evidence if the history shows it | Commit the GitHub era docs first, then the pivot as its own commit |
| 36 | Module 2 (structured output) | The schema changes: categories and flags | Covered once PRD v1.0 exists |
| 37 | Module 5 (retrieval) | **The docs don't exist yet.** A fictional bank's help center must be written, which is real PM work and can balloon | Cap at about 10 short articles. Never copy a real bank's pages |
| 38 | Module 9 (gold set) | **CFPB complaints are formal complaints to a regulator, not first messages to a bank's chat.** They skew severe and long, so the escalation rate on this data will run far higher than a real inbox | State it as an assumption. Build the gold set from real complaint categories plus short chat style rewrites. Category labels come from CFPB. Must escalate labels come from Subhasish's policy judgment, written before the first run |
| 39 | Module 9 (production monitoring) | No real customers means no real traffic after deployment | A replay job sends gold set messages into Chatwoot on a schedule, so monitoring has something to watch |
| 40 | Module 10 (red team) | New cases: social engineering ("I'm her husband, what's her balance"), phishing lures, requests for account actions, messages full of personal data | Add to the five negative paths |
| 41 | Content and README | Consumer narratives are published by CFPB, but quoting individuals in posts is still wrong | Aggregate statistics only, never quote a narrative |
| 42 | Brand and ethics | A realistic bank site could be mistaken for a real one | Obviously fictional name, "fictional bank, demo only" on every page |
| 43 | Employer boundary | Bank complaints sit closer to the old employer's world than GitHub did | No student loans, no former employer flows or policies as templates, fictional bank only. Rule added to project instructions |
| 44 | Stakeholders | Finance adds a stakeholder GitHub didn't have: compliance | The escalation policy (item 14) is the compliance artifact. Subhasish signs it off as policy owner |
| 45 | Phase A budget | Chatwoot setup, the bank docs and the Lovable page add about 3 to 4 hours. Dropping the GitHub App saves 1 to 2 | Net +2 hours on a 15 hour budget. Cut docs to 10 articles to hold it |
| 46 | Interview window | The interview prep chat reads STATE.md | No action beyond updating STATE.md |

---

## Decisions needed before PRD v1.0

1. **Name:** DECIDED 20th Sept. Warmhand (agent), Kettlewick Bank (fictional).
2. **Fictional bank name.**
3. **Product scope:** credit cards and bank accounts only. Excludes student loans, mortgages, crypto, remittances.
4. **Chatwoot:** free cloud plan if agent bots work on it, else self host.
5. **The 10 help articles:** who drafts. Recommendation: Subhasish outlines, Claude drafts, Subhasish edits. It is product work, not code.

## Execution order

| Step | Who | What |
|---|---|---|
| 0 | Subhasish, Claude Code | Add LICENSE, commit GitHub era docs, create the public repo, push |
| 1 | Claude | STATE.md, `.env.example`, `.gitignore`, archive the GitHub brief |
| 2 | Subhasish | Answer the decisions, write the regulated support brain dump |
| 3 | Claude | PRD v1.0, escalation policy, syllabus, handoff, project instructions |
| 4 | Subhasish | Paste project instructions and description into claude.ai |
| 5 | Claude | Stage 2 redo for fintech support agents |
| 6 | Both | Stages 3 and 4 |
| 7 | Subhasish, Claude Code | Commit the pivot as one clear commit, then Module 1 |
