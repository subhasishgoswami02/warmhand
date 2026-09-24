# Warmhand: from zero to production, and after

**Version 2, 19th September 2026.** Rewritten for the pivot to bank complaint triage. Version 1 (GitHub issue triage) is in git history at commit `58ef2f1`.

## What you will have at the end

A production agent that sits behind a fictional bank's support chat. A customer types a message. Warmhand masks any card or account numbers, works out what the complaint is about, checks it against the escalation policy, and either answers from the bank's own help articles with citations, or hands the conversation to a human with a private note explaining why. It never asks for sensitive data, never promises money, and fails by handing off, never by going silent. Every decision is logged without personal data. A nightly job re-runs a gold set built from real public complaints (CFPB) and blocks any prompt change that makes it worse.

**Agent = model + harness.** You rent the model. Everything you build in this course is the harness: prompts, tools, orchestration, code checks, retrieval, logging, evals and deployment.

## How you learn each module

Every module runs the same loop. Skipping a step is how "it worked" gets mistaken for understanding.

| Step | What happens | Why |
|---|---|---|
| 1. Concept | Claude explains the idea in plain words, before any command | You can't debug what you can't picture |
| 2. Predict | You write one line: what you expect to happen | Wrong predictions are where the learning is |
| 3. Type | You type the code yourself in Claude Code. No pasting finished modules | Reps. The point is your hands, not the artifact |
| 4. Prove | Run the module's proof | If you can't show it, it isn't done |
| 5. Break | Break it on purpose once (bad key, bad input, kill the network) | Production is mostly the unhappy paths |
| 6. Explain back | Three sentences per concept, in your own words | A fuzzy explanation means fuzzy understanding |
| 7. Commit | A small commit with a message a hiring manager could read | The history is part of the evidence |
| 8. Write | One post while the detail is fresh | Content never gets batched at the end |
| 9. Update STATE.md | What changed, what's next | So no window ever has to re-learn the project |

## Packaging as you go: recipes

Every module's proof becomes a small standalone recipe in `recipes/`, with a README, runnable in five minutes: `recipes/01_first_api_call`, `02_card_masking`, `02_forged_citation_test`, `03_tool_allowlist`, `05_citation_check`, `06_chatwoot_webhook`, `09_regression_gate`. One build, a dozen showable pieces, each one the proof under a post. The format is borrowed from awesome-llm-apps.

## The rules

1. You type the code. Claude explains, reviews and unblocks.
2. Every module ends with a proof and an explain back.
3. No employer data, ever. Public data (CFPB) and synthetic cases only. Fictional bank only. No student loans.
4. No secrets in git. Public repo, MIT licensed.
5. Never claim something shipped when it is designed.

---

## Part 0: Product (the PM work, done before and alongside code)

| Step | What | Concepts | Status |
|---|---|---|---|
| 0.1 | Problem and PRD | Problem vs solution, users, goals and non goals, hypotheses vs evidence, metrics with definitions | GitHub version done, bank version next |
| 0.2 | Competitive analysis | Demand side competition, the same feature test, moat vs feature, counter positioning, positioning statement | GitHub version done and archived, bank version next |
| 0.3 | The pivot | Killing an idea on evidence, change mapping in two passes | Done |
| 0.4 | Escalation policy | Writing a policy the code must obey. Compliance as a stakeholder. Regulatory clocks, vulnerable customers | Next |
| 0.5 | Flows, user stories, acceptance criteria | Given, when, then. Happy path, error states, edge cases | Stage 3 |
| 0.6 | Technical discovery | Can the APIs actually do what the flows need? Validation tasks before building | Stage 4 |
| 0.7 | The help articles | Writing the ~10 articles the bot answers from. Knowledge base ownership is product work | Before Module 5 |

---

## Phase A: the demo (Modules 1 to 6, about 17 to 19 hours)

The original 15 hour budget grew with the pivot: the Chatwoot setup, writing the help articles and the Lovable page add about 3 to 4 hours, and dropping the GitHub App saves 1 to 2.

### Module 0: Foundations (done, two gaps left)

| Concepts | Terminal basics, virtual environments, environment variables, `.env` vs `.env.example`, `.gitignore`, why a deleted secret is still in git history, commit hygiene |
|---|---|
| **Gaps to close** | MIT `LICENSE` file, a public GitHub repo with the remote pushed, a Claude Code hook that blocks committing `.env` |
| **Proof** | `git status` never lists `.env`. The repo is public with a license. The hook refuses a test commit of `.env` |
| **Explain back** | What a venv protects you from. Why `.env.example` is committed and `.env` is not. Why deleting a committed key doesn't make it safe |
| **PM lens** | Secret hygiene is a governance control, not a developer chore |

### Module 1: The API call

| Concepts | HTTP request and response, methods, headers, status codes, JSON. API keys and auth headers. Tokens: input, output, context window. Cost per call. Latency. Model parameters: system prompt, temperature, max tokens. Errors: 400, 401, 429, 500, 529. Timeouts. Retries with exponential backoff and jitter. Raw HTTP vs the SDK |
|---|---|
| **Build** | One raw request to the model API, then the same call through the SDK. The task: categorize one real CFPB credit card complaint |
| **Proof** | You can read a 429 and explain exactly what your client must do next, and you can state the cost of one categorization |
| **Break it** | Wrong key, then an impossible max tokens value |
| **PM lens** | Unit economics per conversation. Where latency comes from |
| **Post** | What actually happens when you call a model API, for product people |

### Module 2: Structured output, and what belongs to code

| Concepts | Why free text breaks systems. Schemas. Pydantic models. Enums for categories and risk flags. Validation. The repair loop (send the error back, retry, give up after N). Failing closed. Prompt versioning (prompts as files with versions). **Deterministic pre-processing:** masking card numbers (with a checksum test), account numbers and emails in plain code, before the model ever sees them. Unit tests with pytest |
|---|---|
| **Build** | A schema for category plus flags (including the fraud intake note, where every field allows "unknown"), validated output, a repair loop, a masking function with tests. **Tests use a fake model with real API calls switched off**, so they're free and repeatable. The first adversarial test: a fake model returns a forged citation, and the answer must be refused |
| **Reference** | `references/awesome-llm-apps/rag_tutorials/agentic_typed_rag_pydanticai` (`agent.py`, `test_typed_rag.py`). Read it, then type your own version |
| **Proof** | A deliberately malformed model response is caught and repaired, not passed on. A message containing a card number reaches the model masked |
| **Break it** | Feed it a response with a category that isn't in the enum |
| **PM lens** | A schema is a contract between systems. Deciding what the model is allowed to judge and what code decides is the core product call |
| **Skill loaded here** | `engineering:testing-strategy` |
| **Post** | Why free text output breaks production systems, and the repair loop that fixes it |

### Module 3: Tools and the agent loop

| Concepts | Tool definitions (name, description, input schema). The loop: the model asks for a tool, your code runs it, the result goes back, repeat until done. Stop conditions and max iterations. Read tools vs write tools. Side effects. Idempotency keys. **The model proposes, code disposes:** the executor checks every requested action against an allowlist |
|---|---|
| **Build** | Two tools: `search_help_docs` (read) and `propose_action` (reply, handoff, note), with an executor that enforces the allowlist |
| **Proof** | The model picks the right tool, and running the same request twice doesn't act twice |
| **Break it** | Prompt it to request an action outside the allowlist. The executor refuses |
| **PM lens** | Blast radius. Every write tool is a liability you choose to take on |
| **Skill loaded here** | `lenny-building-with-ai-agents` |
| **Post** | Tool calling explained without the hype, including what idempotency costs you |

### Module 4: Graph orchestration

| Concepts | **Workflow vs agent:** a workflow follows paths you wrote, an agent picks its own path. Warmhand is mostly a workflow with one agentic step, on purpose. State machines. LangGraph: state, nodes, edges, conditional edges (routers), checkpoints, interrupts for human in the loop. Deterministic nodes vs model nodes. Multi agent patterns (orchestrator and workers, maker and checker) and when not to use them |
|---|---|
| **Build** | The triage graph: mask, classify, check the policy, retrieve, draft, verify, act or hand off, log. The escalation branch, and an interrupt where a human can approve |
| **Reference** | `references/awesome-llm-apps/rag_tutorials/corrective_rag`: retrieve, grade, then branch. Copy the shape, change the fallback. Theirs searches the web. A bank must never do that, so ours hands off |
| **Proof** | You draw the graph on paper first, and the code matches the drawing |
| **Break it** | Force a classification error and watch which branch it takes |
| **PM lens** | Decomposing a workflow: which steps belong to the model and which to rules. This is the decomposition case study, done for real |
| **Skills loaded here** | `lenny-building-with-ai-agents`, `engineering:system-design` |
| **Post** | Decomposing a support workflow into a graph: what belongs to the model, what belongs to rules |

### Module 5: Retrieval

| Concepts | Writing the knowledge base (the ~10 help articles, before any code). Chunking. Keyword search first (BM25), then embeddings and vector similarity, then hybrid. Top k. Grounding. Citations, and checking in code that every cited passage was actually retrieved. Abstaining when nothing supports an answer. Retrieval evals (did the right passage come back?) |
|---|---|
| **Build** | Search over the fictional bank's articles, a relevance gate before the model, answers with verbatim quote citations checked in code, a handoff when unsupported |
| **Reference** | `references/awesome-llm-apps/rag_tutorials/rag_failure_diagnostics_clinic`: 12 failure patterns (P01 to P12) as a debugging checklist |
| **Proof** | It answers from the docs with a correct citation, and hands off when the docs don't cover the question |
| **Break it** | Ask something the docs almost cover. Does it bluff? |
| **PM lens** | Retrieval is not truth. The knowledge base is a product with an owner, and stale docs make confident wrong answers |
| **Post** | Retrieval is not truth. Grounding, citations, and saying I don't know |

### Module 6: The real system (Chatwoot)

| Concepts | Webhooks (push) vs polling. Payload anatomy. A public URL for your laptop (tunnels). Proving a request is genuine (signatures and HMAC, or the shared secret fallback). Idempotency by message ID. Eligibility filters (incoming customer messages, one inbox). Conversation states: pending (bot) and open (human). Handoff. Private notes. Labels. **Shadow mode:** the would-be reply posted as a private note. The race check (did the customer write again while you were drafting?). Failing closed means handing off. A watchdog for conversations stuck in pending |
|---|---|
| **Build** | Chatwoot inbox, the agent bot, a one page fictional bank help site built in Lovable with the chat widget, the webhook receiver, and the full path live |
| **Proof** | A message typed into the bank's widget gets a cited reply, or a handoff with a private note explaining why |
| **Break it** | Send the same webhook twice. Kill the model mid request. Send two messages in a row |
| **PM lens** | Integration risk. Operational states. What the human agent sees when the bot steps aside |
| **Post** | Wiring an agent to a real helpdesk, and why shadow mode saved me |

**End of Phase A:** the 60 second demo. One message answered with a citation, one handed off with its reason visible.

---

## Phase B: production (Modules 7 to 10)

### Module 7: MCP

| Concepts | What the Model Context Protocol is. Server vs client. Tools, resources and prompts. Transports (local stdio vs HTTP). Tool schemas |
|---|---|
| **Build** | An MCP server exposing Warmhand's triage and policy check tools |
| **Proof** | You drive your own agent from Claude, by name |
| **PM lens** | MCP as distribution: your capability shows up inside other people's agents |
| **Post** | MCP in plain English, with a server you can read in one sitting |

### Module 8: Production

| Concepts | Service structure. Configuration per tenant. Secrets in a real secret store. Health checks. Acknowledge the webhook fast, process in the background (queues). Postgres. Deployment and rollback. Structured logs. A scheduler for the watchdog. Service level objectives |
|---|---|
| **Build** | The FastAPI service deployed with a public webhook URL. Optional: a hash chained decision log, where each entry stores hashes of the masked input and output plus the previous entry's hash, so tampering is detectable |
| **Reference** | `references/awesome-llm-apps/advanced_ai_agents/multi_agent_apps/trust_gated_agent_team` (the `AuditTrail` class) |
| **Proof** | It works with your laptop closed |
| **PM lens** | "Production" means someone else can depend on it. SLOs are promises |
| **Skill loaded here** | `engineering:deploy-checklist` |
| **Post** | What production actually means for an agent |

### Module 9: Observability and evals in production

| Concepts | Traces and spans. Metrics: latency, cost, action rate. **The gold set:** sampling real CFPB complaints, labeling categories (from CFPB) and must escalate (from the policy, by you), freezing labels before the first run. Eval types: code assertions, LLM as judge, human labels. Calibrating the judge against your labels. Confidence intervals (why 0 out of 50 means "likely under about 6%", not zero). A regression gate in CI that blocks prompt changes. A replay job sending gold set messages into Chatwoot, so production has traffic to monitor. Alerting. Drift |
|---|---|
| **Build** | Traces, the nightly eval job, the gate. Then **the checker experiment:** add a second agent that verifies each answer against its citations and the policy, and compare with and without it on the gold set |
| **Proof** | You deliberately degrade a prompt and the gate blocks it. The checker stays only if it cuts wrong answers at an acceptable cost and latency |
| **PM lens** | Evals are the acceptance criteria of an AI product. Multi agent is a hypothesis you test, not a style you adopt |
| **Skill loaded here** | `lenny-ai-evals` |
| **Post** | Evals in production: the gate that blocked my own prompt change |

### Module 10: Red team and release discipline

| Concepts | Failure injection (model down, timeouts, malformed output). Prompt injection. Fraud patterns: scams in progress, account takeover, fake staff. Social engineering ("I'm her husband, what's her balance?"). Phishing lures. Messages full of personal data. Fallbacks. Prompt versioning, changelog, rollback. A release decision memo. An incident runbook |
|---|---|
| **Build** | At least five negative paths, each with a test and a user facing response |
| **Proof** | Every failure path has a test and a safe, visible outcome |
| **PM lens** | The risk register becomes executable |
| **Post** | I red teamed my own bank bot. Here's what broke |

---

## Phase C: packaging and launch

### Module 11: Package and launch

| Concepts | README as a product page: the problem, the demo, a harness map, "why not X", limitations, "fictional bank, not financial advice". An architecture diagram that matches the code. Positioning |
|---|---|
| **Build** | README, a 60 second recording, the diagram, a Lovable page showing public eval results, launch posts, and a **pull request to awesome-llm-apps** adding Warmhand as a regulated support agent with an escalation policy and eval gate (acceptance isn't guaranteed) |
| **Proof** | A stranger installs and runs it from the README alone |
| **Skill loaded here** | `engineering:documentation` |

### Module 12: Monetisation, honestly assessed

Credibility into offers first, consulting inbound (fintech support deployments) second, open core third, a helpdesk marketplace app fourth. Build so paths three and four stay open: config per tenant, no personal data in the schema, a clean service boundary. No billing until a stranger asks to pay.

---

## After launch: operating it (the "and later")

| Rhythm | What you do | Concept |
|---|---|---|
| Nightly | The gate runs. Read failures, never mute them | Regression discipline |
| Weekly | Review escalations and costs. Did the bot hand off things it should have answered? | Precision vs coverage, tuned with evidence |
| On every prompt or model change | Version it, run the gate, write one changelog line | Change management |
| When something breaks | Follow the runbook, write a short blameless postmortem | Incident response (`engineering:incident-response`) |
| When a model is deprecated | Swap it in config, rerun the gate, compare cost and quality | Vendor risk |

---

## Tools, and why each one is here

| Tool | Where | Why |
|---|---|---|
| Claude Code | Everywhere | Where you type and commit. It is itself a harness |
| Anthropic API | Modules 1 onward | The model |
| LangGraph | Module 4 onward | Orchestration with state, branches and human interrupts |
| Chatwoot | Module 6 onward | The real helpdesk and handoff |
| Lovable | Module 6 (bank help page), Module 11 (eval results page) | Front ends you don't need to hand code |
| CFPB complaint API | Module 1 (one example), Module 9 (gold set) | Real, labeled, public data |
| Render or Railway | Module 8 | Hosting. Decided in Stage 4 |
| Tracing tool (Langfuse, LangSmith or PostHog) | Module 9 | Decided in Stage 4 |
| Fin (Product Pass) | Optional, after Module 9 | Benchmark against a commercial agent |
| Not used | n/a | Obsidian, Graphify, n8n, Replit, Hermes Agent. Each solves a problem this project doesn't have |

## What this maps to, for interviews

- Coding plus design: Modules 1 to 5 are the conversation.
- Decomposition: Module 4 is a decomposed workflow with routing and human checkpoints.
- Founder or CTO: Modules 9 and 10. Almost nobody brings evals and rollback to an agent demo.

## Order matters

Don't skip ahead to the graph because it sounds more interesting than retries. Most agent demos fall over in production because of Modules 1, 2 and 3, not Module 4.
