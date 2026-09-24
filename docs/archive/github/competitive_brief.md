# FirstPass competitive brief

**Researched:** 19th September 2026. All sources are public web pages, listed at the end. Vendor claims are marked as claims.

## 1. Executive summary

**The biggest threat:** GitHub already ships the core safety pattern FirstPass was going to be known for. GitHub Agentic Workflows (public preview since June 2026) runs the agent read only and routes every write through "safe outputs": label allowlists, per run caps, allowed domains, and a threat detection job. "Hard limits in code" is not a moat. It is table stakes, set by the platform owner.

**The biggest signal:** Dosu, the best known AI triage bot for open source, moved away from issue triage in August 2026, citing agent generated pull requests as the new flood. Standalone issue triage is not a strong business.

**The opportunity:** nobody in this set publishes how often their bot is wrong, or measures when it should have stayed quiet. Outcome priced support vendors (Zendesk charges per automated resolution) are paid for answering, not abstaining. An open, evaluation first reference build with its results in public is unclaimed ground, and it is exactly what the portfolio goal needs.

## 2. Demand side view: what a maintainer uses if FirstPass vanished

| Alternative | Reality |
|---|---|
| Doing it by hand | The default for most small projects |
| Issue templates and forms | Free, prevents missing info at the source |
| GitHub Agentic Workflows starter triage | Native, free to try, labels plus a free text comment |
| A hosted bot (Dosu, Pullfrog, Kapa) | Less setup, less control |

For most maintainers, templates plus GitHub's own starter workflow is good enough. FirstPass's most real audience is the evaluator of this artifact.

## 3. The ten competitors, with the same feature test

**Same feature test:** if a well funded competitor shipped this exact feature tomorrow, what would still be ours? A differentiator that fails is a feature, not a moat.

| # | Competitor | What they do | Differentiator 1 | Differentiator 2 | Differentiator 3 | Verdict |
|---|---|---|---|---|---|---|
| 1 | **GitHub Agentic Workflows** (GitHub Next, public preview June 2026) | Agents in Actions, read only, writes via safe outputs with label allowlists, caps, allowed domains, threat detection. Starter triage workflow labels and posts an unrestricted comment | Answers only when the docs support it, checked in code. Their starter comment is free text | A published eval gate with adversarial cases, blocking prompt regressions | An opinionated escalation matrix, not a general toolkit | **All three fail.** Each is a workflow GitHub or a user could add. Strongest competitor by far |
| 2 | **Dosu** | Auto answers and labels issues, learns from corrections, claims 5,955+ installed repos. Moved to agent knowledge infrastructure in August 2026, free tier limits from 1st September | Precision first: silence unless cited. Dosu markets closing issues before you see them | A visible decision log per issue | Open source and self hostable | **Fail.** Dosu open sourced its labeler and has left the category |
| 3 | **Pullfrog** (Colin McDonnell, beta May 2026) | Open source, bring your own key, Actions based agent bot. Triage is one of eight modes. Free for open source, Pro $30 a month per org. Dosu's migration partner for triage | Single purpose triage with an explicit handoff policy | Eval gate | Model free text limited to one path | **Fail.** A config and prompt change for them |
| 4 | **Anthropic claude-code-action triage example** | Official example workflow: labels new issues, no comments. Issues write, contents read | Answers questions with citations | Code allowlist tighter than the token's scope | Eval gate | **Fail**, trivially copyable. Note: Anthropic's own choice is label only, which supports the conservative stance |
| 5 | **LLM labeler actions** (GitHub's AI labeler and moderator, OpenAI issue labeler, AI Labeler) | Classify and label with an LLM. GitHub's versions ran on GitHub Models, retired 30th July 2026 | No dependence on a free platform inference tier that can disappear | Answers plus escalation, not labels only | Eval gate | **Partial.** Point 1 is real resilience, not a moat |
| 6 | **Astro triagebot-action** | Reproduces bugs, diagnoses, attempts fixes, opens fix branches, drives a label state machine | No code access at all, so a far smaller blast radius | Cheaper per issue, no reproduction sandbox (unverified) | Eval gate | **Survives as counter positioning** for point 1: their value is fixing code, so they won't give up code access |
| 7 | **Kapa.ai** | Docs Q&A for developer tools. GitHub Action auto posts answers with up to five citations, has an uncertainty flag, skips bug and feature issues by default. Paid, demo led | Code checks every citation was actually retrieved | Free and self hosted | Security, abuse and injection routing | **Fail.** Kapa already does cited answers with an uncertainty flag. Point 2 is a price position, not a moat |
| 8 | **Linear Triage Intelligence** | Suggests team, assignee, labels, duplicates. Per property "suggest or auto apply". Shows its reasoning. Business and Enterprise plans | Works in public on untrusted input from strangers | Replies to reporters, not just routing | Free and open | **Fail as a moat**, different context. Worth stealing: per property suggest versus auto apply |
| 9 | **Intercom Fin** | Support AI agent. $0.99 per outcome, including resolutions and handoffs. A resolution means no further help requested after Fin's last answer | Public forum context | Measures wrong answers, not resolution rate | Free and open | **Fail.** Different market. Useful as a contrast in metrics |
| 10 | **Zendesk AI agents** | Automated resolutions included per plan, then $1.50 to $2.00 each (per a third party guide) | Not paid per answer, so no pressure to answer | Abstention measured and published | Free and open | **Point 1 survives as counter positioning.** A vendor billing per resolution won't sell silence |

**Adjacent reference, not a competitor:** Decagon describes layered guardrails (regression tests before release, bad actor detection and escalation rules during, automated review after). That is the enterprise version of FirstPass's shape, which is useful evidence that the pattern transfers.

## 4. What survives the same feature test

| Candidate moat | Survives? | Why |
|---|---|---|
| Hard limits in code | **No** | GitHub ships it as safe outputs |
| Cited answers | **No** | Kapa ships it |
| Eval gate | **No** as a mechanism | Anyone can build one |
| **Public, versioned eval history** (gold set, nightly results, decision logs) | **Yes, weakly** | History dependent. It can't be backfilled, only earned by publishing consistently over time |
| **Counter positioning against per resolution pricing** | **Narrowly** | Applies to outcome priced support vendors, not to free GitHub tools |
| **No code access, by design** | **Narrowly** | Only against fix-it bots like triagebot |

**Honest conclusion:** as a product, FirstPass has no durable moat, and competing with GitHub on GitHub is a losing position. As a portfolio artifact, the one surviving asset (public evidence of evaluation discipline) is exactly the thing that proves the builder's skill.

## 5. Positioning recommendation

**For** people evaluating how to ship support deflection agents safely, **FirstPass is** an open reference implementation of a triage agent **that** publishes when it stays quiet and how often it is wrong, **because** every decision is logged and every prompt change runs through a public regression gate.

| Choice | Recommendation |
|---|---|
| Category | Don't fight "AI triage bot". Own "evaluation first reference build" |
| Porter's two paths | Differentiation through transparency. Never on cost, where GitHub is free |
| What to say about GitHub | Name it. The README gets a "Why not GitHub Agentic Workflows?" section: for most repos, use it. FirstPass shows the full stack end to end and publishes its evals, and its policy can be ported into a gh-aw workflow |
| What to steal | gh-aw's separate threat detection step, Linear's visible reasoning and suggest versus auto apply, Kapa's default skip of bug and feature issues (already in V0) |
| What not to claim | That FirstPass invented code enforced limits, or that it is "better than" any product. It has no users |

**Market signal to watch, not to build:** the pain is shifting from issues to AI generated noise. curl reported useful bug bounty reports falling from about 15% to 5% before ending its bounty. A future FirstPass could route low quality reports to `needs-info`, but it stays out of V0.

## 6. Battlecard: FirstPass vs GitHub Agentic Workflows

**Who asks:** an interviewer or a maintainer. This is the question you will get.

| Capability | FirstPass | gh-aw | Winner |
|---|---|---|---|
| Write limits enforced outside the model | App permissions plus code allowlist | Read only agent plus safe outputs, allowlists, caps, domain filter | **Tie**, and theirs is platform grade |
| Grounded answers | Citation required and checked in code | Starter comment is free text, grounding left to the user | **FirstPass**, but copyable |
| Regression gate on prompt changes | Built in, nightly, public | Not built in | **FirstPass**, copyable |
| Setup | Install an App plus host a service | A markdown workflow in the repo | **gh-aw** |
| Maturity and support | One builder, no users | GitHub | **gh-aw** |
| Scope | Issue triage only | Any repo automation | **gh-aw** for breadth, **FirstPass** for focus |

**Where FirstPass wins:** it shows the whole stack (webhook, orchestration graph, retrieval, deployment, evals) instead of hiding it in a platform, and it publishes its failure rate.

**Where gh-aw wins:** zero ops, native, free to start, and backed by GitHub. Counter: don't contest it. Recommend it for most repos and show you understood why its design is right.

| They say | Say |
|---|---|
| "Why not just use GitHub Agentic Workflows?" | "For most repos, you should. I built FirstPass to own every layer myself and to publish the evals. GitHub's safe outputs use the same principle as my rule set: the model proposes, code decides what is allowed" |
| "Isn't this just a demo?" | "Yes, and it says so. What isn't a demo is the gate: here's the prompt change it blocked" |
| "How do you know it's safe?" | "I don't claim safe. I claim zero wrong answers on 50 frozen cases, which means likely under about 6%, and here's the log" |

**Questions that show depth:** "How do you know your triage bot's wrong answer rate?" "What does your bot do when the model is down?" "Who decides when it should stay quiet?"

**Win or lose:** wins when the evaluator values depth and evidence. Loses when the need is a zero maintenance tool for one repo.

## 7. OKR options (next ~8 weeks)

Three equal options, each at roughly 60 to 70% confidence.

**Option A: credibility**
Objective: make FirstPass the clearest proof that I can ship a production agent end to end.
- The Phase A demo is recorded and linked from the README by the end of week one
- At least 3 interview conversations go deep on the repo, eval gate or escalation matrix
- 1 person who has never spoken to me runs FirstPass from the README alone

**Option B: quality**
Objective: a triage agent that is never wrong in public.
- 0 wrong public answers on the 50 case gold set for 14 consecutive nightly runs
- 100% of must escalate cases escalated across those runs
- Action rate rises 10 points from its first measured baseline with both gates still passing

**Option C: reach**
Objective: be known for evaluation first agents, not just for having built one.
- 6 posts published, each linking to a commit that proves its claim
- 1 inbound conversation (role or consulting) that cites the content
- 1 maintainer who is not me installs the App on a real repo

**Assumption flagged:** Options A and C depend on data only you can observe (interviews, inbound). Track them in a private note, never in the public repo.

## Sources

- GitHub Agentic Workflows, safe outputs: https://github.github.com/gh-aw/reference/safe-outputs/
- GitHub Agentic Workflows public preview: https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview/
- gh-aw Issue Triage workflow: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows/
- Dosu for OSS: https://dosu.dev/oss
- Dosu, "OSS has changed. So has Dosu.": https://dosu.dev/blog/oss-has-changed-so-has-dosu
- Pullfrog comparisons: https://docs.pullfrog.com/comparisons
- Pullfrog on InfoQ: https://www.infoq.com/news/2026/05/pullfrog-ai-github/
- claude-code-action triage example: https://github.com/anthropics/claude-code-action/blob/main/examples/issue-triage.yml
- GitHub AI labeler and moderator: https://github.blog/changelog/2025-09-05-github-actions-ai-labeler-and-moderator-with-the-github-models-inference-api/
- GitHub Models retired: https://github.blog/changelog/2026-07-30-github-models-is-now-retired/
- Astro triagebot-action: https://github.com/withastro/triagebot-action
- Kapa GitHub issue responses: https://www.kapa.ai/blog/automating-github-issues-responses-with-kapa
- Linear Triage Intelligence: https://linear.app/docs/triage-intelligence
- Fin pricing: https://fin.ai/pricing
- Zendesk automated resolutions (third party guide): https://www.eesel.ai/blog/zendesk-automated-resolutions
- Decagon layered guardrails: https://decagon.ai/resources/designing-layered-guardrails-for-reliable-ai-agents
- Jeff Geerling, "AI is destroying Open Source": https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/
