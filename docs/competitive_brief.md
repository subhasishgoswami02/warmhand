# Warmhand competitive brief: AI support agents for banks

**Researched:** 21st September 2026. Sources at the end. Vendor claims are marked as claims, third party pricing as third party.

## 1. Executive summary

**Biggest threat:** Chatwoot, the helpdesk Warmhand runs on, ships its own AI agent, **Captain**, which learns from the help center and hands off to humans. A real bank on Chatwoot would switch Captain on before building anything. It's the same pattern as last time: the platform owner already covers the basic job.

**Second threat:** the market leader already claims what we planned to claim. Intercom's **Fin** advertises "Procedures" with deterministic controls for dispute workflows, full audit trails, ISO 42001 certification, quarterly adversarial testing, and a claimed hallucination rate of about 0.1%. Guardrails in code, audit logs and measured accuracy are table stakes at the top of this market.

**The opportunity:** every vendor publishes claims. None publishes the test set. The regulator has already said in writing what goes wrong with bank chatbots: in its 2023 report, the CFPB flags wrong answers, **failing to recognize disputes unless specific words are used**, doom loops with no route to a human, and privacy and phishing risks. An open, reproducible benchmark built from the CFPB's own public complaint data, with the escalation mapping published, that tests exactly those failures, is unclaimed. It is also what the portfolio needs.

## 2. Demand side: what a bank uses if Warmhand vanished

| Alternative | Reality |
|---|---|
| Humans only | Still common, expensive, slow at peaks |
| The helpdesk's built in AI (Chatwoot Captain, Zendesk AI, Fin inside Intercom) | The default for most. Switched on, not built |
| A banking specialist (Kasisto, Posh, interface.ai) | Credit unions and community banks buy these |
| An enterprise platform (Sierra, Decagon, Agentforce) | Large institutions, long deployments |
| Build in house | The largest banks (Bank of America's Erica is the best known) |

No bank would pick Warmhand over these. Its real audience is people evaluating how to deploy these agents safely: hiring managers, CX and compliance leaders, and the builder's own interviews.

## 3. Ten competitors, with the same feature test

**Test:** if a well funded competitor shipped this exact feature tomorrow, what would still be ours?

| # | Competitor | What they do | Differentiator 1 | Differentiator 2 | Differentiator 3 | Verdict |
|---|---|---|---|---|---|---|
| 1 | **Chatwoot Captain** | AI agent inside Chatwoot. Learns from the help center, past conversations and FAQs, hands off to humans, has a Copilot for agents. Paid plans include AI credits | Citations on every answer, checked in code (its page mentions no source attribution) | A published escalation policy for regulated cases | An open test set | **All fail.** Each is a feature Chatwoot could add. Strongest threat |
| 2 | **Intercom Fin** | Leading support agent. $0.99 per outcome. Claims about 0.1% hallucination, "Procedures" with deterministic controls for disputes and KYC, full audit trails, ISO 42001, AIUC-1 adversarial testing | Handoff recall measured on regulator derived cases | Fixed templates for sensitive moments | Open, reproducible results | **1 and 2 fail** (Procedures cover them). **3 survives:** Fin publishes rates, not the test set |
| 3 | **Zendesk AI agents** | Automated resolutions included per plan, then $1.50 to $2.00 each (third party guide) | Not paid per answer | Measures correct handoffs, not containment | Open benchmark | **1 survives as counter positioning:** a vendor paid per resolution won't sell escalation |
| 4 | **Decagon** | Enterprise support agents. Layered guardrails: regression tests before release, bad actor detection and escalation rules during, automated review after. About $50k platform fee plus $0.50 per resolution (third party) | Same layers, built in the open | Regulator derived test set | Free | **Fail.** Decagon has the same shape. Useful proof the pattern is right |
| 5 | **Sierra** | Enterprise agents, financial services use cases. About $150k a year plus implementation, 3 to 7 month deployments (third party) | Readable in a day, not 3 to 7 months | Open test set | Free | **Fail as a moat.** Different buyer entirely |
| 6 | **Salesforce Agentforce** | $2 per conversation (third party). CRM native | Helpdesk agnostic | Open test set | Free | **Fail.** Different buyer |
| 7 | **Kasisto (acquired by Backbase)** | Banking specialist. KAIgentic platform, KAI-GPT, multiple agents coordinating "to avoid hallucinations", compliance positioning | Transparent, published policy | Open test set | Free | **3 fails, 1 and 2 are positioning** |
| 8 | **Posh** | Banks and credit unions. Answers, routine tasks, handoff with full context. Advertises containment "up to 99%" | Optimizes for correct handoff, not containment | Legal clock triggers | Open test set | **1 survives as counter positioning:** containment is their headline metric. The CFPB's doom loop concern is the opposite |
| 9 | **interface.ai** | Agentic AI for credit unions and community banks, including a collections agent and an agentic contact center platform | Never moves money, by design | Open test set | Free | **1 is a deliberate limit, not a moat** |
| 10 | **In house assistants** (for example Bank of America's Erica) | Built by the largest banks on their own data | Published method | Portable | Free | **Fail.** Different league |

## 4. What survives

| Candidate | Survives? | Why |
|---|---|---|
| Guardrails in code, fixed templates | **No** | Fin Procedures, Decagon layers |
| Warm handoff with context | **No** | Posh, Captain and Fin all claim it. The name describes the value, but it isn't a moat |
| Citations | **No** | A feature anyone can add |
| **An open, reproducible handoff benchmark** built from public CFPB complaints, with the policy mapping and results published | **Yes** | Vendors publish claims, not test sets. Publishing failure cases carries liability they won't take on, and the results history can only be earned, not copied |
| **Measuring correct handoffs instead of containment** | **Narrowly** | Counter positioning against vendors whose headline metric is containment or resolutions |

**Conclusion:** as a product, Warmhand has no moat, and it shouldn't pretend to. As a portfolio artifact, the benchmark is the asset. It turns "I built a bank bot" into "I built the test the regulator's own concerns imply, and published it."

## 5. Positioning

**For** people deploying or evaluating AI support in regulated finance, **Warmhand** is an open reference agent and handoff benchmark **that** shows, on real public complaint data, which conversations a bank bot must never own and whether it hands them off, **because** the escalation policy, test set and results are all published and reproducible.

**Mapped to the CFPB's own chatbot concerns (June 2023 report):**

| CFPB concern | Warmhand's answer |
|---|---|
| Wrong answers | Answers only from cited help articles, with citations checked in code. Zero wrong answers gate |
| Failing to recognize disputes unless the right words are used | Two nets: a keyword floor in code plus the model reading for meaning. Either one hands off. 100% recall gate on disputes |
| Doom loops, no way to reach a human | One bot reply, then a human. A watchdog opens any stuck conversation within 5 minutes |
| Privacy and phishing risk | Sensitive numbers masked before the model and the logs. Code blocks any request for a PIN, CVV, passcode or card number |

This table goes in the README. It's the strongest single framing the project has.

**What not to claim:** that Warmhand beats any vendor, that it's compliant (it's a demo on a fictional bank), or that containment is bad. The claim is narrower: the handoff decision deserves its own published test.

## 6. Battlecard: Warmhand vs Intercom Fin

**Who asks:** an interviewer, a CX leader, or a compliance lead.

| Capability | Warmhand | Fin | Winner |
|---|---|---|---|
| Deterministic controls on sensitive workflows | Code allowlist, fixed templates | Procedures with deterministic controls | **Tie.** Fin's is production grade |
| Hallucination control | Answers only with retrieved and checked citations | Proprietary retrieval, reranking and validation. Claims about 0.1% | **Fin**, at scale |
| Audit trail | Decision log without personal data | Full audit trails | **Tie** |
| Certifications | None, it's a demo | ISO 42001, SOC 2, others | **Fin** |
| Published test set and results | Yes, built from public CFPB data | Claims only | **Warmhand** |
| Headline metric | Correct handoffs | Resolutions, $0.99 each | Depends on what you're protecting |
| Cost and time to understand | Free, readable in a day | Per outcome, enterprise onboarding | **Warmhand** for learning, **Fin** for running a bank |

| They say | Say |
|---|---|
| "Why not just use Fin, or Captain?" | "If I ran support at a bank, I'd start there. Warmhand exists to show how the handoff decision should be tested, on the regulator's own data, in the open. It's a benchmark you can point any vendor at" |
| "Fin already claims 0.1% hallucination" | "On their test set. Mine is public. Run Fin against it and publish the result. I'd like to see it" |
| "Is this compliant?" | "No, and it doesn't claim to be. It's a demo on a fictional bank. What it shows is the method: policy, test set, gate" |

**Questions that show depth:** "What's your bot's handoff recall on disputes, and on what test set?" "What does it do when the model is down?" "Who owns the escalation policy, and how does a change get released?"

## 7. OKR

Already decided (quality plus credibility): ship from scratch to production, never wrong in public, and prove it. Stage 2 adds one key result for the benchmark: **the gold set, the policy mapping and the results are published in the repo in a form a stranger can re-run.**

## Sources

- Chatwoot Captain: https://www.chatwoot.com/captain
- CFPB, "Chatbots in consumer finance" (June 2023): https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/
- Fin, AI agent compliance for financial services: https://fin.ai/learn/evaluate-ai-agent-compliance-financial-services
- Fin pricing: https://fin.ai/pricing
- AI agent pricing in 2026 (third party): https://www.thewitn.com/blog/ai-agent-pricing-in-2026-what-fin-sierra-decagon-and-agentforce-actually-charge
- Zendesk automated resolutions (third party): https://www.eesel.ai/blog/zendesk-automated-resolutions
- Decagon layered guardrails: https://decagon.ai/resources/designing-layered-guardrails-for-reliable-ai-agents
- Kasisto: https://kasisto.com/
- Posh digital assistant: https://www.posh.ai/digital-assistant
- interface.ai: https://interface.ai/
- Sierra, financial services: https://sierra.ai/blog/five-ways-to-use-ai-agents-financial-services
