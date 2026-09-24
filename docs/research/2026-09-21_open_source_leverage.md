# Open source leverage and the portfolio playbook, 21st September 2026

## 1. What Shubham Saboo's GitHub actually is

- **Who:** Senior AI Product Manager at Google Cloud, 9.5k GitHub followers, co-author of two AI books, runs the Unwind AI newsletter.
- **The asset:** one mega repo, `awesome-llm-apps` (about 135k stars, 20k forks, Apache 2.0). It holds 100+ small runnable apps in about 14 categories.
- **The engine:** new templates every week, pushed through the newsletter and social. A catalog plus distribution, sustained over time.

**Categories:** Agent Skills, Starter Agents (single file, API key only), Advanced single agent apps, Multi agent apps, Always on (scheduled) agents, Multi agent teams, Voice agents, Generative UI, MCP agents, RAG (20+ variants), Apps with memory, "Chat with X", LLM cost optimization, Fine tuning, Framework crash courses (Google ADK, OpenAI Agents SDK).

**Typical app:** one folder, a README, `requirements.txt`, a Streamlit UI, runnable in minutes. **Deliberately shallow:** no evals, no deployment, no monitoring, rarely any guardrails. For example, the Customer Support Voice Agent (Firecrawl, Qdrant, FastEmbed, GPT-4o, TTS) has no escalation to a human at all.

**Lesson:** there are two credibility plays. The **breadth catalog** (Saboo) wins stars and reach. The **depth reference build** (Warmhand) wins trust with people hiring for production roles. You can't out-breadth a 135k star repo, and you don't need to. You can borrow its format.

## 2. Borrowing the format, without new scope

| Idea | What it means | Cost |
|---|---|---|
| **Recipes folder** | Every module's proof becomes a small standalone recipe: `recipes/01_first_api_call`, `02_repair_loop`, `02_card_masking`, `03_tool_allowlist`, `05_citation_check`, `06_chatwoot_webhook`, `09_regression_gate`. Each has a README and runs in five minutes | Near zero. The proofs already exist. It's packaging |
| **One post per recipe** | Already the content track | None |
| **Contribute to `awesome-llm-apps`** | Phase C: open a pull request adding "Regulated support agent with escalation policy and eval gate". It fills a visible gap (their support agent has no handoff) | One PR. Acceptance isn't guaranteed |

## 3. Warmhand's coverage of the same categories

| Saboo category | Warmhand | Where |
|---|---|---|
| Advanced single agent | Yes | Modules 3 to 6 |
| Multi agent | Yes, the checker agent experiment | Module 9 |
| RAG | Yes, with citations checked in code | Module 5 |
| MCP | Yes | Module 7 |
| Always on agents | Yes: the watchdog, the nightly gate, the replay job | Modules 8 and 9 |
| Generative UI / frontends | Partly: the Lovable bank page and eval page | Modules 6 and 11 |
| Cost optimization | Partly: cost per conversation tracked | Modules 1 and 9 |
| Memory across sessions | **No, by design.** A bank bot should not remember customers across sessions in V0 | Non-goal |
| Voice | No | Possible V2 |
| Fine tuning | No | Not needed |

One build covers seven of the categories, all at production depth.

## 4. What to leverage directly

**Rule: borrow patterns, not code, for anything on the learning path.** You type those. Use a library directly only for commodity infrastructure, and even then only after writing the naive version once, so you know what the library is doing for you.

| Source | What to take | Where | How |
|---|---|---|---|
| **openai/openai-cs-agents-demo** (MIT, about 6.6k stars) | A customer service triage agent handing off to specialists, with "relevance" and "jailbreak" guardrails, a FastAPI backend and a Next.js UI | Modules 3 and 4 | Read and compare. Different SDK, same shape. Good contrast: its handoffs go between agents, ours go to humans |
| **LangGraph's official customer support example** (`langgraph/examples/customer-support`) | Human in the loop interrupts before sensitive tools | Module 4 | Read before building the graph |
| **anthropics/courses**: prompt engineering tutorial, tool use, prompt evaluations | The concepts behind Modules 1, 2, 3 and 9 | Before each module | Read, run the notebooks |
| **anthropics/claude-cookbooks**, `tool_use` folder | Tool use and structured output patterns with Claude | Modules 2 and 3 | Read |
| **microsoft/presidio** | Detecting and masking personal data (names, emails, phone numbers, card numbers) | Module 2 | Write your own card number masking first (checksum and all), then use Presidio for the rest and compare |
| **promptfoo** | Open source evals and red teaming, runs in CI | Modules 9 and 10 | Write your own small gate first. Then use promptfoo's red team plugins to attack Warmhand |
| **Langfuse** | Open source tracing and evals, cloud or self hosted | Module 9 | The likely answer to the open "which tracing tool" question. Stage 4 confirms |
| **awesome-llm-apps: RAG Failure Diagnostics Clinic** | A list of 12 RAG failure patterns (P01 to P12: grounding drift, chunk boundaries, stale index, and more) | Modules 5 and 9 | Use as a debugging checklist |
| **awesome-llm-apps: Trust-Gated Multi-Agent Team** | A tamper evident audit log: each log entry includes the hash of the previous one, so editing history breaks the chain | Module 8 or 9 (optional) | About 15 lines. Makes the decision log verifiably untampered. A strong compliance talking point |
| **awesome-llm-apps: Knowledge Graph RAG with Citations, Typed Agentic RAG with Pydantic AI** | Citation handling, typed agent outputs | Modules 2 and 5 | Read |
| **CFPB ccdb5-api** | The complaint data | Modules 1 and 9 | Use directly |

## 5. Lenny

Lenny Rachitsky's own GitHub has one public repo, a Prince of Persia tribute page. Nothing to leverage. The Lenny value is the Product Pass tools (already mapped) and community projects such as `lenny-mcp`, an MCP server over the podcast transcripts. It's a readable example of a small MCP server for Module 7, and useful for content research.

## Sources

- https://github.com/Shubhamsaboo
- https://github.com/Shubhamsaboo/awesome-llm-apps
- https://github.com/openai/openai-cs-agents-demo
- https://github.com/langchain-ai/langgraph/blob/main/examples/customer-support/customer-support.ipynb
- https://github.com/anthropics/courses
- https://github.com/anthropics/claude-cookbooks
- https://github.com/microsoft/presidio
- https://www.promptfoo.dev/docs/red-team/
- https://github.com/langfuse/langfuse
- https://github.com/lennysan
- https://github.com/akshayvkt/lenny-mcp
