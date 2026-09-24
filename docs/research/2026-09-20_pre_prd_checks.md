# Pre PRD checks, 20th September 2026

Three checks run before PRD v1.0. Two of them change a decision.

## 1. The name "FirstPass" collides inside banking

First Financial Bank (US) already uses **FirstPass** as the name of its voice biometrics login, a product that controls customer access to accounts. A demo bank support agent with the same name, in the same industry, invites confusion with a real bank's security product. There is also an unrelated FirstPass AI (hiring software).

**Recommendation:** rename. Candidates checked by web search on 20th September 2026:

| Name | Meaning | Collision found |
|---|---|---|
| **Warmhand** | From "warm handoff": passing a customer to a human *with context*. That is the product's whole point, and the private note makes it literal | None found in AI or banking |
| Stepaside | Knows when to step aside | Place name in Dublin only, no product found |
| Firstline | First line of support | **Taken** (an AI agent for IT service desks, plus several support AI firms) |
| Keep FirstPass | n/a | A real bank's authentication product |

**Fictional bank name candidates:**

| Name | Collision found |
|---|---|
| **Brindlecove Bank** | None |
| Norvale Bank | Only a fantasy wiki place and an unrelated club |
| Kestrel Bank | **Real financial firms** use Kestrel (Kestrel Wealth Management, a division of KS Bank, and others). Avoid |

A web search is not a trademark search. Fine for a portfolio demo, not for a company.

## 2. Chatwoot Cloud's free plan no longer allows API or webhooks

On 16th July 2026 Chatwoot restricted API and webhook access to paid plans, citing spam and misuse. The free Hacker plan can't run an external bot. Self hosted Chatwoot keeps full API and webhook access.

| Option | Cost | Effort | Learning |
|---|---|---|---|
| **Chatwoot Cloud, Startups plan** | $19 per agent per month, one agent. Start on the 15 day free trial to validate the bot flow before paying | Lowest. No servers | Standard SaaS integration |
| Self hosted on the Mac with Docker (Phase A), then hosted for Phase B | Free locally. Phase B needs hosting for Chatwoot itself (Rails, Postgres, Redis, Sidekiq) | Higher. Several containers, and a second system to keep alive in production | Docker, running someone else's service |

**Recommendation:** Cloud Startups, starting with the free trial. The goal is to learn agents, not to operate a helpdesk. Docker is still worth learning, and it comes up in Module 8 for FirstPass's own service. Whether agent bots are included on Startups is a Stage 4 check, done inside the trial.

## 3. What real complaint data says about escalation

CFPB complaints received from 1st September 2025 to date, pulled from the public API on 20th September 2026.

**Credit cards: 98,125 complaints.** The largest issues:

| Issue | Count | Must escalate under the draft policy? |
|---|---|---|
| Problem with a purchase shown on your statement (disputes, charges not made) | 30,329 | **Yes**, billing dispute or unauthorized charge |
| Getting a credit card (includes 7,976 "card opened without consent") | 11,347 | Partly, the opened without consent share is identity theft |
| Other features, terms, or problems | 10,778 | Mostly no (rewards, service) |
| Fees or interest | 9,729 | No, often answerable from docs, but never promise a refund |
| Incorrect information on your report | 9,272 | **Yes**, a credit reporting dispute |
| Closing your account | 6,727 | Depends |
| Problem when making payments | 4,876 | Mostly no |
| Problem with company investigation | 4,710 | **Yes**, an open dispute |
| Advertising and marketing | 4,197 | No |
| Trouble using your card | 3,742 | Mostly no |
| Struggling to pay bill (1,240 "won't work with you during hardship") | 1,407 | **Yes**, hardship |

**Under the draft mapping, about 56% of credit card complaints (55,129) fall into must escalate categories:** disputes, unauthorized or unconsented accounts, credit report disputes, open investigations, hardship, identity theft and fraud alerts.

**Checking and savings accounts: 89,008 complaints.** "Transaction was not authorized" alone is 10,327. Counting only the top named sub-issues (unauthorized transactions, accounts opened without consent, money taken on the wrong day or for the wrong amount), **at least 16% (14,301)** must escalate. The real share is higher, because the largest issue, "Managing an account" (51,521), wasn't broken down past its top two sub-issues.

**What this means for the product:**
1. Precision over coverage isn't a stance, it's what the data demands. On credit cards, the majority of real complaints are ones a bot must never resolve alone.
2. These are formal complaints to a regulator, skewed toward the unresolved and severe. A real chat inbox will have a far larger share of simple questions. That's an assumption to state, not a finding.
3. **A first post the data supports:** "More than half of credit card complaints fall into categories an AI must never resolve alone," with the mapping published so anyone can check it.

**Caveat:** the 56% and 16% depend on my draft mapping of CFPB issues to "must escalate". The mapping becomes final only when the escalation policy is signed off.

## Sources

- First Financial Bank, FirstPass voice biometrics: https://ffin.com/contact-us/voice-biometrics
- FirstPass AI: https://firstpassai.com/
- Firstline: https://www.firstline.so/
- Kestrel Wealth Management rebrand: https://bizfayetteville.com/banking-finance/2026/1/12/ks-trust-and-wealth-management-rebrands-as-kestrel-wealth-management-a-division-of-ks-bank-inc/5065
- Chatwoot, "Updating API and Webhook Access on Chatwoot Cloud": https://www.chatwoot.com/blog/updating-api-and-webhook-access-on-chatwoot-cloud
- Chatwoot pricing: https://www.chatwoot.com/pricing
- CFPB complaint search API: https://cfpb.github.io/ccdb5-api/
