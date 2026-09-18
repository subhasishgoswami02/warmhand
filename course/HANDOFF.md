# Handoff: read this first

A fresh session starts here. Everything needed to continue is in this file plus `SYLLABUS.md`.

## Who this is for

Subhasish Goswami. Senior product leader, 14 years, fintech and applied AI. Not an engineer, and does not want to be treated as one, but wants real hands-on reps: agentic loops, graph orchestration, MCP, API keys, deployment, post-production monitoring.

**Working preferences:** no em dashes anywhere. No sugarcoating, no generic advice. Direct, friend-like tone. Short and punchy over comprehensive. Tables for comparisons. Hinglish is welcome in conversation.

## What we are building

A GitHub issue triage agent. A live webhook receives issues from a repo, an agent classifies them, retrieves context from that repo's own documentation, drafts a response, decides whether it may act alone or must escalate to a human, writes labels and comments back to GitHub, and logs every decision. A nightly job re-runs a gold set and blocks a prompt change that degrades quality.

Same shape as an enterprise support-deflection deployment. Public data, so it can be published.

## Decisions already locked

| Decision | Choice | Why |
|---|---|---|
| Domain | GitHub issue triage | Real API, public data, publishable, mirrors enterprise support deflection |
| Language | Python | What he can already read, and where the agent tooling lives |
| Graph | LangGraph | State, conditional edges, checkpoints, human in the loop |
| Service | FastAPI | Webhook endpoint |
| Storage | SQLite first, Postgres at deploy | Do not over-build early |
| Deploy | Render | Free tier, public URL, simple |
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

Scaffolded, nothing built:

```
~/Developer/triage-agent/
  .gitignore
  .env.example
  course/
    SYLLABUS.md      ten modules, content track, monetisation view
    MODULE_00.md     foundations, ready to run
    HANDOFF.md       this file
```

**Not done yet:** Module 0 has not been run. No venv, no git init, no PRD, no brain dump, no code.

## The immediate next action

Two open threads, in this order:

1. **The PRD.** Stage 1 of the idea-to-prototype skill. Three questions to him: product name, what it does in one sentence, and a raw brain dump. Produce `brain_dump.md` and a **lean** `prd.md`: problem, users, MVP scope, success metrics, risks. Defer pricing, distribution and full competitive analysis to modules 11 and 12, because writing a pricing section before the first API call is fiction. Then run skill stages 2 to 4 (differentiation, flows and user stories, technical discovery). **Skip stages 5 and 6**, which produce a design system and a mocked frontend and would send this sideways.
2. **Module 0.** Commands are in `MODULE_00.md`. Proof: `git status` must not list `.env`.

## Portfolio and monetisation stance

This is a portfolio artifact and possibly a product. Public repo, README that grows per module, one content piece per module (Substack long, LinkedIn short).

On money, the honest ranking: credibility into job offers first, consulting inbound second, open core third, GitHub Marketplace app fourth. Probability of meaningful revenue is low. Probability of changing how an interviewer sees him is high. Build for the second, keep the door open for the first: per-tenant config rather than hardcoding, no personal data in the schema, clean service boundary. No billing until a stranger asks to pay.
