# FirstPass PRD

**Status:** Draft v0.3, 19th September 2026. v0.2 was revised after a multi persona review, and v0.3 adds the competitive analysis. Stage 2 of 4. Nothing here is built yet except the repo skeleton.
**Owner:** Subhasish Goswami (product, build, and every decision below).

**One line:** FirstPass does the first pass on every new GitHub issue, labeling it and answering from the project's own docs, and hands it to a maintainer when it can't cite an answer or the call isn't its to make.

**Descriptor:** An AI agent for GitHub issue triage that knows when to hand off.

---

## 1. Summary

FirstPass is a GitHub App that reads each new issue on a repository, labels what kind of report it is, and either posts one reply backed by the project's own docs or hands the issue to a human maintainer. Its hard limits live in code, so a manipulated model still cannot close, delete or rewrite anything. Every decision is logged, and a regression gate blocks prompt changes that make it worse.

**Operating principle:** precision over coverage. Escalating too much is acceptable at launch. Being confidently wrong in public is not.

## 2. Background and why now

**Context.** Open source maintainers (often 1 to 5 people, often volunteers) do the first pass on every issue by hand: work out what it is, ask for missing details, point to docs, and route the real bugs. Help today is issue templates, rule based labelers, and a growing set of AI triage bots. Stage 2 maps them.

**Why now.** Models can now call tools and return structured output reliably enough that a narrow, auditable agent is buildable by one person. The market moved in 2026 too. GitHub put the same safety pattern into its own platform (Agentic Workflows, public preview June 2026). Dosu, the best known open source triage bot, moved away from issue triage in August 2026. Triage bots are becoming a free platform feature, so FirstPass does not compete as a product. It competes as evidence: an open reference build that publishes when it stays quiet and how often it is wrong. See section 12.

**Why now for the builder.** Hands-on reps with agents in production (orchestration, retrieval, evals, deployment) while between roles, producing public evidence rather than claims.

## 3. Goals and non-goals

### Product goals

1. Reporters with a question the docs already answer get a cited reply without waiting for a human
2. Bug reports missing basic details get a precise request for those details, in minutes
3. Maintainers get a filterable queue (`needs-maintainer`) of the issues that genuinely need judgment
4. FirstPass never makes the project look wrong in public

### Builder goals (the real reason this exists)

1. **Demo:** two live issues, one answered with a citation and one escalated with its reason logged, shown in under 60 seconds of screen recording. End of Phase A
2. **Gate:** a deliberately degraded prompt is visibly blocked by the regression gate. Phase B
3. **Reproducible:** a stranger installs and runs it from the README alone. Phase C
4. **Honest content:** one public post per build step, and no post claims more than the repo shows

### Non-goals

| Non-goal | Why |
|---|---|
| Closing or resolving issues | Irreversible and trust destroying if wrong |
| Multi turn conversation | Doubles the injection surface. V1 at the earliest |
| Duplicate detection | Needs search over issue history. V1 |
| Pull requests and code | A different risk class entirely |
| Dashboard or UI | GitHub labels plus the decision log are enough |
| Multiple repos in production, billing | No demand yet. Revisit when a stranger asks |

## 4. Problem

Every row below is a **hypothesis**, not validated data.

| Hypothesis | Why it matters | How we check |
|---|---|---|
| A large share of new issues are questions the docs already answer | Answerable from docs means automatable with a citation | Sample ~100 closed issues from the test library and count |
| Many bug reports arrive missing version, logs or steps | A request for missing details is safe and fast | Same sample |
| First response is slow because triage is batched | Reporters give up or open duplicates | Time to first maintainer comment in the same sample |
| Maintainers distrust bots that answer confidently and wrongly | A wrong public answer costs more than no answer | Stage 2 research on how existing bots are received |

**Evidence task:** the 100 issue sample is owned by Subhasish, done during Stage 2. It gives the problem section real numbers and makes a good first post.

## 5. Users

| User | Needs | What FirstPass gives them in V0 |
|---|---|---|
| **Maintainer** (primary) | Less sorting, no embarrassment from a bot speaking for the project | Report type labels, safe replies, and a `needs-maintainer` queue. The reason for each escalation is in the decision log. V0 has no private channel to show it on GitHub |
| **Reporter** (secondary) | A fast, correct first response | A cited answer, or a precise request for missing details |
| **Evaluator of this artifact** (honest third audience) | Proof the builder understands production agents | Public repo, installable app, logged decisions, a regression gate, a release memo |

## 6. Solution (V0)

### Identity: a GitHub App

FirstPass runs as a GitHub App, so its comments show as `firstpass[bot]`, never as a person.

| Why an App | Detail |
|---|---|
| Clear identity | Its comments can never be confused with a maintainer's, which rule 7 depends on |
| Least privilege | It asks only for Issues (read and write) and Metadata (read). No code access at all |
| No long lived token | It exchanges a private key for short lived tokens per installation. The key is the one secret to guard |
| Scales without rework | Any repo owner can install it. Multi repo becomes configuration, not a rebuild. It is also the GitHub Marketplace path |

### Events it listens to

| Event | Why |
|---|---|
| New issue opened | The main path |
| New comment created | Only to flag reporter follow ups (rule 7). It never replies to comments |

Everything else is ignored.

### Classification: two separate questions

1. **Report type:** bug report, feature request, question, or unclear
2. **Risk flags:** possible security report, abusive content, instructions aimed at the bot, author is a maintainer, author is a bot

"Unclear" means the model said so, or its output failed validation. V0 has no numeric confidence score.

### What it does, per case

| Case | Labels | Comment |
|---|---|---|
| Possible security report | `needs-maintainer` | Fixed security template (rule 2) |
| Abusive content, or instructions aimed at the bot | `needs-maintainer` | None |
| Author is a bot, or a maintainer (configurable) | None | None |
| Question, and retrieved docs support an answer | `question` | One cited answer. **The only path where the model writes free text** |
| Question, docs don't support an answer | `question`, `needs-maintainer` | None |
| Bug report missing version, logs or steps | `bug-report`, `needs-info` | Fixed template listing exactly which details are missing |
| Bug report with the basics | `bug-report` | None. Whether it is really a bug is the maintainer's call |
| Feature request | `feature-request` | None (rule 3) |
| Unclear | `needs-maintainer` | None |
| Any error: model down, timeout, invalid output | `needs-maintainer` if possible | None, ever. Logged |

Labels describe what was **reported**, not a verdict. Labeling something `bug` would publicly rule that it is one.

**Allowed labels, fixed set:** `bug-report`, `feature-request`, `question`, `needs-info`, `needs-maintainer`.

### The never-do rules

**Code** means a hard check before any GitHub write, holding even if the model is fully manipulated. **Prompt** means the model is instructed. Prompt rules are wishes, code rules are guarantees.

| # | Rule | Enforced by |
|---|---|---|
| 1 | FirstPass can only **add a label from the fixed set** and **post its own comment**. It never closes, reopens, locks, deletes, transfers or pins an issue, and never edits or removes anyone's comment or label. The App's permissions are the outer wall, the code allowlist the inner one | App permissions plus code allowlist |
| 2 | On a possible **security report** it writes nothing about the content, applies no security label, and generates no text. It adds `needs-maintainer` and posts one fixed template: "Thanks for the report. If this involves a security vulnerability, please don't add further details here. A maintainer will follow up." plus a pointer to `SECURITY.md` when the repo has one | Prompt to detect, code to force the template |
| 3 | It never **commits the project to a decision**: no promising or rejecting features, no timelines, no ruling on "bug or intended behavior" | Prompt, labels by report type, gold set cases |
| 4 | Every **factual claim** in an answer must be backed by a doc passage it actually retrieved, and it links that passage. No supporting passage, no answer: escalate. Requests for missing details come from a fixed template and need no citation | Code checks every cited link is in the retrieved set. Evals check the passage supports the claim |
| 5 | It never responds to **abusive content** and never moderates. It escalates. A frustrated reporter with a real problem is triaged normally | Prompt, gold set cases |
| 6 | It acts **only on issues**. New issue events never include pull requests, but comment events and GitHub's issue list API do, so every comment event is checked explicitly. It never touches code, branches or merges | Code, plus the App has no code permission |
| 7 | **At most one FirstPass comment per issue, ever.** A repeated webhook delivery never produces a second comment. When anyone other than FirstPass or a maintainer comments after FirstPass has commented, FirstPass adds `needs-maintainer` and says nothing. It ignores its own comments, other bots, and edits | Code: records handled event and issue IDs before any write |
| 8 | **Issue text is data, never instructions.** Nothing in an issue changes what FirstPass may do. Comments may only link to the repo's own docs. Model written text appears in exactly one path, the cited answer. Every other comment is a fixed template filled by code | Code for everything it can reach, prompt for the rest, injection cases in the gold set |

**Escalation is a label, not a ping.** FirstPass never @mentions anyone.

### Operations

- **Dry run:** every write can be switched to "log only". On by default until the live path is proven
- **Kill switch:** suspend the App's installation or disable its webhook in GitHub settings. No deploy needed
- **Decision log:** stores issue number, event ID, report type, flags, decision, reason, retrieved passage IDs, model and prompt version, latency and cost. It does **not** store usernames or issue bodies. Usernames are used at runtime only (bot and maintainer checks) and never saved
- **Configurable per repo, not hardcoded:** label names, docs location, whether to skip maintainer authored issues, dry run on or off

### Test environment

A sandbox repo Subhasish owns, with the App installed, containing the docs of a small, permissively licensed Python library, and synthetic issues modeled on that library's real public issues. Real issues are read, never written to. In the sandbox, "skip maintainer authored issues" is off so that the owner's own demo issues get triaged.

## 7. Success metrics

### Hard gates, on the gold set

The gold set is synthetic issues, each with its **expected report type, flags, action and, for questions, the expected answer, written before the first run**. Phase A uses ~20 cases run by hand. Phase B grows it to ~50, with at least 10 adversarial (security, abuse, injection, PR comments, duplicate deliveries), run nightly.

| Gate | Target | Definition |
|---|---|---|
| Wrong public answers | 0 | A posted answer where any claim isn't supported by its cited passage, or contradicts the expected answer. Judged by Subhasish in Phase A, an LLM judge checked against his labels in Phase B |
| Must escalate cases escalated | 100% | Security, abuse, injection, unsupported questions, follow ups |
| Duplicate comments under replayed deliveries | 0 | Same event sent twice or more |
| Writes outside the allowlist | 0 | Any API call other than add label or create comment |

**Honest limit:** 0 wrong out of 50 does not prove the rate is zero. It shows the true rate is likely under about 6%. The gate is necessary, not sufficient.

### Tracked, no target in V0

| Metric | Definition |
|---|---|
| Action rate | Share of eligible issues where FirstPass posted an answer or a needs-info request. Low is acceptable at launch, loosened only with eval evidence |
| Report type accuracy | Match against the expected type on the gold set |
| Time to label | Event received to FirstPass's label, under 2 minutes for 95% of events |
| Cost per issue | Ceiling set once the first real API call is measured |

### After real traffic, lagging signals

Maintainer label changes on FirstPass labeled issues (disagreement), and reporter follow ups after an answer (a sign the answer didn't help). Not measurable in the sandbox, so not claimed.

## 8. Release

| Phase | Scope | Budget | Proof |
|---|---|---|---|
| **A: Demo** | Model calls, structured output, tools, the triage graph with escalation, retrieval with citations, live GitHub App on the sandbox repo, dry run | Week one, ~15 hours | Builder goal 1 |
| **B: Production** | MCP interface, deployment with a public webhook, nightly eval gate, failure injection, release memo | After Phase A | Builder goal 2 |
| **C: Packaging** | README, recording, architecture diagram, launch posts | After Phase B | Builder goal 3 |

Phases map to course modules 1 to 6, 7 to 10, and 11 in `course/SYLLABUS.md`. Anything in Phase B or C is labeled "next" in the README until it exists.

**Roadmap beyond V0:** V1 adds duplicate detection and answering follow ups, earned by the gold set passing with zero wrong answers for two weeks. V2 lists the App publicly for other repos, earned by a maintainer who is not the builder asking to use it. V3 is a hosted version, earned by someone asking to pay.

## 9. Assumptions

| Assumption | Status | Checked in |
|---|---|---|
| Issues (read and write) plus Metadata (read) permissions are enough to label and comment | To verify | Stage 4 |
| The chosen library's docs are markdown and licensed for copying with attribution | To verify | Stage 4 |
| Webhooks can reach a local machine through a tunnel during Phase A, before deployment | To verify | Stage 4 |
| Issues are in English | Accepted limit | n/a |
| Model cost is low enough to run the gold set nightly | To verify | First API call |
| Maintainers want this at all | Unvalidated | Stage 2 |

## 10. Risks and mitigations

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Confidently wrong public answer | High | Medium | Rule 4, zero tolerance gate, model free text in one path only |
| Escalates almost everything | Medium | High at launch | Accepted by design. Track action rate, loosen only with evidence |
| Prompt injection through issue text | High | Medium | Rule 8, App permissions, code allowlist, adversarial gold set cases |
| Double posting from webhook retries | Medium | High without a fix | Rule 7 idempotency check |
| App private key or API key leaked | High | Low | Never in git, secret store at deploy, key rotation documented |
| Phase A overruns 15 hours | High | High | Phase A is the only commitment. B and C are labeled "next", never implied as done |
| Docs out of date, so cited answers are wrong | Medium | Medium | The exact passage is cited so the reporter can judge. Stale docs detection is V1 |
| Webhook tunnel unreliable during Phase A | Low | Medium | Dry run and replayed deliveries for development, live only for the demo |
| GitHub Agentic Workflows makes FirstPass redundant for most maintainers | High | High, already true | Position as a reference build plus public evals, not a product. The README says plainly when to use GitHub's tool instead |
| A vendor retires the model or platform FirstPass depends on (GitHub Models was retired 30th July 2026) | Medium | Medium | Bring your own model key, with the model name in config

## 11. Open questions

| # | Question | Owner | Blocking? |
|---|---|---|---|
| 1 | Which library's docs to use | Subhasish, with Claude | Blocks retrieval. Stage 4 |
| 2 | Are the needs-info fields (version, logs, steps) generic, or per repo config | Subhasish | No. Stage 3 |
| 3 | Where a security escalation is seen privately beyond the label | Subhasish | No. Phase B |
| 4 | Run the 100 issue evidence sample | Subhasish | No, but it gates any public claim about the problem. Stage 2 |

## 12. Competitive landscape

Full brief with sources, a battlecard and OKR options: `docs/archive/github/competitive_brief.md`. Researched 19th September 2026.

| # | Competitor | What they do | Same feature test |
|---|---|---|---|
| 1 | GitHub Agentic Workflows | Read only agents in Actions, writes limited by "safe outputs" (label allowlists, caps, allowed domains, threat detection) | FirstPass's code enforced limits **fail**. GitHub ships them |
| 2 | Dosu | Auto answers and labels. Left issue triage in August 2026 | Fail. The category leader exited |
| 3 | Pullfrog | Open source, bring your own key, multi mode agent bot, free for open source | Fail. Triage policy is a config change for them |
| 4 | Anthropic claude-code-action triage example | Labels only, never comments | Fail, copyable. Supports the conservative stance |
| 5 | LLM labeler actions | Label with an LLM. GitHub's versions ran on the now retired GitHub Models | Partial. Not depending on a vendor's free tier is resilience, not a moat |
| 6 | Astro triagebot-action | Reproduces, diagnoses and fixes bugs | **Survives narrowly.** FirstPass has no code access by design, and they won't give theirs up |
| 7 | Kapa.ai | Auto posted doc answers with citations and an uncertainty flag | Fail. Cited answers already exist |
| 8 | Linear Triage Intelligence | Suggests routing and duplicates, shows reasoning, suggest or auto apply per property | Fail. Different context. Steal "suggest versus auto apply" |
| 9 | Intercom Fin | Support agent, $0.99 per outcome | Fail. Different market, useful metric contrast |
| 10 | Zendesk AI agents | Paid per automated resolution | **Survives narrowly.** A vendor paid per answer won't sell silence |

**What survives:** only a **public, versioned eval history** (gold set, nightly results, decision logs). It can't be backfilled, only earned by publishing consistently. Everything else is a feature.

**Positioning:** for people evaluating how to ship support deflection agents safely, FirstPass is an open reference implementation of a triage agent that publishes when it stays quiet and how often it is wrong, because every decision is logged and every prompt change runs through a public regression gate.

**Consequences for the build (no new scope):**
- The README gets a "Why not GitHub Agentic Workflows?" section. Honest answer: for most repos, use it
- Never claim FirstPass invented code enforced limits. Say it uses the same principle as GitHub's safe outputs
- Publishing eval results moves from nice to have to the core asset. Phase B's nightly gate results go in the repo

## 13. Deferred sections

| Section | Where | Why not now |
|---|---|---|
| User stories and acceptance criteria | Stage 3 | Needs the flows agreed first |
| Technical approach and feasibility | Stage 4 | Needs the API checks |
| Pricing, distribution | Course modules 11 and 12 | Pricing before the first API call is fiction |
