# Reference code review: what to take from awesome-llm-apps, 22nd September 2026

Eight apps from Shubham Saboo's repo (Apache 2.0) pulled and read line by line. The code lives in `references/awesome-llm-apps/`, which is **gitignored**. It is someone else's code, so it doesn't go into Warmhand's public history. We borrow patterns, and Subhasish types our own version.

## The verdict, ranked by value to Warmhand

| Rank | App | Value | What we take | Module |
|---|---|---|---|---|
| 1 | **Typed Agentic RAG with Pydantic AI** (`rag_tutorials/agentic_typed_rag_pydanticai`) | **Very high.** It is almost exactly our rule 4, done well | Three patterns, below | 2, 5, 9 |
| 2 | **Trust-Gated Multi-Agent Team** (`advanced_ai_agents/multi_agent_apps/trust_gated_agent_team`) | **High** | A hash chained audit log that stores *hashes* of the input and output, not the text | 8 |
| 3 | **Corrective RAG** (`rag_tutorials/corrective_rag`) | **High for Module 4** | A LangGraph graph with a "grade the documents" node and a conditional edge | 4, 5 |
| 4 | **RAG Failure Diagnostics Clinic** (`rag_tutorials/rag_failure_diagnostics_clinic`) | Medium | A 12 pattern failure taxonomy (P01 to P12) for debugging | 5, 9 |
| 5 | **Advisor Orchestrator Worker** skill (`agent_skills/advisor-orchestrator-worker`) | Medium, later | Model tiers: cheap models do the work, a stronger model reviews | 9 (checker) |
| 6 | Customer Support Voice Agent | Low, as code | **A contrast:** a support agent with no route to a human. Good post material | Content |
| 7 | Knowledge Graph RAG with Citations | Low | Needs Neo4j. Too heavy for us. Skip | none |
| 8 | AI Fraud Investigation Agent | Low | A tool design reference, different domain. Skip | none |

## 1. Typed Agentic RAG: three patterns we adopt

**Pattern A: a deterministic gate *before* the model.** It searches first. If the best match scores below a threshold, it refuses **without calling the model at all**. That's zero cost and zero chance of a made up answer on questions the docs don't cover.
Warmhand: if no help article passes the relevance threshold, hand off straight away. The model never sees the question.

**Pattern B: citations must quote the source.** Every citation carries the source, the chunk ID *and a short verbatim quote*. Code then checks that the chunk exists and that the quote (at least 8 characters, whitespace normalized) really appears in that chunk's text. If no citation survives, the answer is refused.
This is **stronger than our PRD's rule 4**, which only checked that the cited article was retrieved. A model can cite the right article and still invent what it says. A verbatim quote check catches that. **PRD rule 4 gets upgraded.**

**Pattern C: tests that never call the real model.** Its test suite switches real model calls off and uses a fake model scripted to misbehave. The best test: the fake model returns a *forged citation* (the doc says "seventy dollars", the model claims "one hundred dollars" and quotes a phrase that isn't there), and the test asserts the answer gets refused.
Warmhand: our adversarial gold set cases become cheap, deterministic unit tests too. This belongs in Module 2 (testing strategy) and saves real money in Module 9.

It also enforces "answered means at least one citation, refused means no citations" inside the output schema itself. That's the Module 2 lesson in one class.

**Different here:** it uses Pydantic AI. We use LangGraph plus the Anthropic SDK. The patterns carry over, the code doesn't.

## 2. Trust-Gated team: the audit log

Each log entry records a sequence number, a timestamp, the action, **a SHA-256 hash of the input and of the output**, and **the previous entry's hash**. A `verify_chain` function recomputes every hash. Edit any old entry and every hash after it breaks.

Why this fits Warmhand unusually well:
- Our log already promises **no message text**. Storing a hash of the message proves which message a decision was about, without keeping the message
- A tamper evident decision log is a real compliance idea. It's about 80 lines
- It's the interview answer to "how would an auditor trust your logs?"

Adopt in Module 8, optional. Still no personal data: hash the *masked* text, never the raw text.

## 3. Corrective RAG: the graph shape

retrieve → grade_documents → (conditional edge) → generate, or → rewrite query → web search → generate.

**Copy the shape, change the fallback.** Their fallback is a web search. A bank must never answer from the open web, so ours is: retrieve → grade → if nothing is relevant, **hand off**. It's a clean first example of a conditional edge for Module 4, and a clear lesson in why domain rules change architecture.

## 4. RAG Failure Diagnostics Clinic

Twelve reusable failure patterns: retrieval hallucination and grounding drift, chunk boundary problems, embedding mismatch, a stale index, query routing errors, long chain reasoning drift, tool misuse, session memory leaks, evaluation blind spots, startup ordering, configuration drift, and multi tenant interference. Use it as a checklist whenever retrieval misbehaves in Module 5, and to tag gold set failures in Module 9.

## 5. Advisor Orchestrator Worker

Its durable rule: **models are knobs, tiers are the architecture.** A strong model advises, cheap models execute, and verification sits between them. For Warmhand: pick the model *per graph node* in config (a cheap one for classification, a stronger one for the answer and for the Module 9 checker). Measure whether it saves cost without failing the gate. Not in Phase A.

## Changes this triggers

| File | Change |
|---|---|
| `prd.md` rule 4 | Citations must include a verbatim quote, checked in code against the chunk text. No surviving citation means a handoff |
| `prd.md` action table | A relevance gate before the model: no article above the threshold means an immediate handoff, with no model call |
| `course/SYLLABUS.md` Module 2 | Tests with a fake model and real calls switched off. First test: a forged citation is refused |
| `course/SYLLABUS.md` Module 4 | Corrective RAG as the reference graph, with "hand off" replacing "search the web" |
| `course/SYLLABUS.md` Module 8 | Optional hash chained decision log |
| `.gitignore` | Add `references/` |
