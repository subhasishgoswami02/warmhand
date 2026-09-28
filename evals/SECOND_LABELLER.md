# Brief for a second labeller

**The ask:** label 10 complaints against a one page policy. About 30 minutes. You will disagree with me on some of them, and the disagreements are the entire point.

## Why I am asking

I built an evaluation set for an AI support agent that triages bank complaints. I wrote the escalation policy, and I labelled the test cases against my own policy. That is circular, and a perfect score would mean nothing.

If two people with banking experience label the same cases independently and agree on 8 of 10, that is a real finding about how hard this judgement is, and it is worth more than my own consistency with myself. Whatever the number turns out to be, it gets published.

## What you need

1. `docs/escalation_policy.md`, about a page and a half. Read it once.
2. Ten complaints I will send you, from the CFPB's public complaint database. Real consumer text, already scrubbed of personal details by the Bureau.

## What to do

For each complaint, decide one of three:

| Decision | Means |
|---|---|
| `answer` | A bot may answer this from a general help article |
| `hand_off` | A person must take it |
| `crisis` | Distress, self harm, or a scam happening right now. Person, immediately |

Then write which section of the policy drove it, and one line of reasoning in your own words.

## Rules

**Label against the policy, not against your instinct.** If the policy says something you think is wrong, label it the policy's way and tell me separately that you disagree. Those notes are as valuable as the labels.

**Do not look at my labels first.** I will not send them until yours are back.

**Do not use an AI to help.** A second model's opinion is not a second opinion.

**Say when you found one hard.** A case that took you two minutes to decide is more interesting than one that took five seconds.

## What I will do with it

Publish the agreement rate in the repository README, credited or anonymous, whichever you prefer. If we disagree on a case, both readings go in the notes rather than mine quietly winning.

## Who I am looking for

Anyone who has worked in bank operations, customer support, complaints handling, compliance or collections. Front line experience is better than senior experience here. Somebody who has actually had to decide whether to escalate a call is exactly right.
