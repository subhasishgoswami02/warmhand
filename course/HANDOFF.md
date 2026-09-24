# Handoff: read this first

**Superseded in parts, 20th September 2026.** The project pivoted from GitHub issue triage to complaint triage for a fictional bank on 19th September 2026. Read `course/STATE.md` first, then `docs/pivot_change_map.md`. Where this file disagrees with STATE.md, STATE.md wins.

A fresh session starts here. Everything needed to continue is in this file plus `SYLLABUS.md`.

## Who this is for

Subhasish Goswami. Senior product leader, 14 years, fintech and applied AI. Not an engineer, and does not want to be treated as one, but wants real hands-on reps: agentic loops, graph orchestration, MCP, API keys, deployment, post-production monitoring.

**Working preferences:** no em dashes anywhere. No sugarcoating, no generic advice. Direct, friend-like tone. Short and punchy over comprehensive. Tables for comparisons. Hinglish is welcome in conversation.

## What we are building

A complaint triage agent behind a fictional bank's support chat. A customer message arrives from Chatwoot (an open source helpdesk) by webhook. The agent masks card and account numbers, classifies the complaint, checks it against a written escalation policy, and either answers from the bank's own help articles with citations or hands the conversation to a human with a private note explaining why. It logs every decision without personal data. A nightly job re-runs a gold set built from real public complaints (the CFPB database) and blocks any prompt change that degrades quality.

This is the same shape as an enterprise support deflection deployment, in a regulated domain, on public data, so it can be published.

## Decisions already locked

| Decision | Choice | Why |
|---|---|---|
| Domain | Complaint triage for a fictional bank (pivoted from GitHub issue triage on 19th September 2026) | Live market, real labeled public data (CFPB), escalation errors carry regulatory weight, the builder's domain edge |
| Live system | Chatwoot | Open source helpdesk, agent bot webhooks, handoff by status change, private notes. Cloud paid plan or self hosted: pending decision |
| Language | Python | What he can already read, and where the agent tooling lives |
| Graph | LangGraph | State, conditional edges, checkpoints, human in the loop |
| Service | FastAPI | Webhook endpoint |
| Storage | SQLite first, Postgres at deploy | Do not over-build early |
| Deploy | Render or Railway | Decided in Stage 4 |
| Model | Anthropic API | He has access |
| Pace | Demo-ready in about a week, roughly 15 hours | An interview round may land |

## Rules of engagement. These matter more than the code.

1. **He types the code.** Explain, review, unblock. Do not paste finished modules for him to nod at. The point is the reps, not the artifact.
2. **Every module ends with a proof.** If he cannot demonstrate it, do not move on.
3. **Every module ends with him explaining the concept back in plain words.** Fuzzy explanation means fuzzy understanding.
4. **No employer data, ever.** Public repos and synthetic cases only. No prompts, documents, customer records or internal names from any employer.
5. **Public repo from commit one.** MIT licensed. Clean history is part of the evidence.
6. **Load skills at the point of need, not up front.** `lenny-ai-evals` at module 9, `lenny-building-with-ai-agents` at modules 3 and 4, `engineering:deploy-checklist` at module 8, `engineering:system-design` at module 4, `engineering:testing-strategy` at module 2, `engineering:documentation` at module 11, `linkedin-post` for the content track.

## Where we are right now

See `course/STATE.md`. It is the only live status file.

## Portfolio and monetisation stance

This is a portfolio artifact and possibly a product. Public repo, README that grows per module, one content piece per module (Substack long, LinkedIn short).

On money, the honest ranking: credibility into job offers first, consulting inbound second, open core third, helpdesk marketplace app fourth. Probability of meaningful revenue is low. Probability of changing how an interviewer sees him is high. Build for the second, keep the door open for the first: per-tenant config rather than hardcoding, no personal data in the schema, clean service boundary. No billing until a stranger asks to pay.
