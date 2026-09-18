# Triage Agent: from zero to production

A hands-on course that builds one real system. You type everything. Nothing is handed to you finished.

## What you will have at the end

A production agent that receives live GitHub issues by webhook, classifies them, retrieves context from the repo's own documentation, drafts a response, decides on its own whether it may act or must escalate to you, writes back to GitHub, and logs every decision. A nightly job re-runs a gold set against it and blocks a prompt change that makes quality worse.

Same shape as an enterprise support-deflection deployment. Public data, so you can publish it.

## The rules

1. You type the code. I explain, review and unblock. I do not paste finished modules for you to nod at.
2. Every module ends with a proof. If you cannot demonstrate the proof, we do not move on.
3. Every module ends with you explaining the concept back in plain words. If the explanation is fuzzy, the understanding is fuzzy.
4. No employer data, ever. Public repos and synthetic cases only.
5. Commit at the end of every module. The git history is part of the evidence.

## The ten modules

| # | Module | Concept you learn | What you build | Proof |
|---|---|---|---|---|
| 0 | Foundations | Why venv, why .env, why .gitignore, how secrets leak | Repo, virtualenv, git, secret hygiene | `git log` shows a first commit and no key is in it |
| 1 | The API call | HTTP, auth headers, tokens, latency, cost, error codes, rate limits, retries with backoff | One raw request to the model API, then the same call via the SDK | You can read a 429 and explain what your client must do |
| 2 | Structured output | Why free text breaks systems. Schemas, validation, the repair loop | Pydantic schema, validated model output, retry-on-invalid loop | A deliberately malformed response is caught and repaired, not passed on |
| 3 | Tools | Tool calling, the agent loop, side effects, idempotency | Two tools the model can choose between, and the loop that runs them | The model picks the right tool, and running the same call twice does not double-act |
| 4 | Graph orchestration | State machines, nodes, conditional edges, checkpoints, human in the loop | The triage graph in LangGraph, with an escalation branch and an interrupt | You can draw the graph on paper and the code matches the drawing |
| 5 | Retrieval | Chunking, embeddings, vector search, grounding, citations, why retrieval is not truth | RAG over a real repo's docs, with citations in the output | The agent answers from the docs and says "I do not know" when the docs do not cover it |
| 6 | The real external system | GitHub API, auth, webhooks, signature verification, idempotency, dry run | Live ingestion from a repo you own, writing labels and comments | A real issue you open triggers a real labeled response |
| 7 | MCP | What the protocol is, server versus client, transports, tool schemas | An MCP server exposing your triage tools, wired into Claude | You drive your own agent from Claude, by name |
| 8 | Production | Config, secrets in a real secret store, health checks, queues, deployment | FastAPI service deployed on Render with a public webhook URL | The webhook works with your laptop closed |
| 9 | Observability and evals in production | Traces, metrics, gold sets, LLM judges, regression gates, alerting | Structured traces, a nightly eval job, release gates wired in | You deliberately degrade a prompt and the gate blocks it |
| 10 | Red team and release discipline | Failure injection, fallbacks, prompt versioning, rollback | Five negative paths, a changelog, a release decision memo | Every failure path has a test and a user-facing response |

## What this maps to, for interviews

- Round 2, coding plus design: modules 1 to 5 are the conversation.
- Round 3, decomposition: module 4 is literally a decomposed workflow with routing and human checkpoints.
- Round 5, founder and CTO: modules 9 and 10. Almost nobody brings evals and rollback to an agent demo.

## Order matters

Do not skip ahead to the graph because it sounds more interesting than retries. The reason most agent demos fall over in production is modules 1, 2 and 3, not module 4.

---

## Public by default

This is a portfolio artifact and possibly a product, not a private exercise. That changes how we build from module 0, not at the end.

**Rules that apply from the first commit:**

1. The repo is public from day one. A clean git history is part of the story, and nobody believes a repo that appears fully formed in one commit.
2. Never a real key, a real customer, or employer data. One leaked key in git history is permanent and public.
3. Every module produces a README section as it lands, not a documentation sprint at the end.
4. MIT license, a clear problem statement at the top of the README, and a demo people can watch in under a minute.
5. Commit messages written as if a hiring manager will read them, because one might.

## The content track

One build session produces one piece of content. Do not batch this at the end, the details go stale and the posts get generic.

| Module | The post that comes out of it |
|---|---|
| 1 | What actually happens when you call a model API, for product people |
| 2 | Why free-text output breaks production systems, and the repair loop that fixes it |
| 3 | Tool calling explained without the hype, including what idempotency costs you |
| 4 | Decomposing a workflow into a graph: what belongs to the model, what belongs to rules |
| 5 | Retrieval is not truth. Grounding, citations, and saying I do not know |
| 6 | Wiring an agent to a real system, and why dry run mode saved me |
| 7 | MCP in plain English, with a server you can read in one sitting |
| 8 | What production actually means for an agent |
| 9 | Evals in production: the gate that blocked my own prompt change |
| 10 | I red-teamed my own agent. Here is what broke |

Substack gets the long version. LinkedIn gets the short version plus the artifact. The repo is the proof under both.

## Module 11: Package and launch

- README with problem, demo, architecture diagram, setup, limitations
- A 60 second screen recording of a real issue being triaged
- Architecture diagram that matches the code
- Landing page, one screen, what it does and who it is for
- Launch on LinkedIn, Substack, and one maintainer community
- **Proof:** a stranger can install and run it from the README alone

## Module 12: Monetisation, honestly assessed

Four paths, in descending order of realistic return for you:

1. **Credibility to offers.** This artifact in interviews and on your profile. Highest value by a distance, and the reason we are building it. Treat revenue as a bonus.
2. **Consulting inbound.** "The person who builds production agents with evals" is a positioning that generates enquiries. The content track does this work.
3. **Open core.** Free self-hosted, paid hosted version. Real but slow. Needs users before it needs pricing.
4. **GitHub Marketplace app.** Cleanest distribution, per-repo pricing, and the hardest, because it needs an app not a script, plus support.

We build so that path 3 and 4 stay open: config per tenant rather than hardcoded, no personal data in the schema, a clean service boundary. We do not build billing until someone asks to pay.

**The honest read:** the chance this earns meaningful revenue is low. The chance it changes how interviewers see you is high. Build it for the second, keep the door open for the first.
