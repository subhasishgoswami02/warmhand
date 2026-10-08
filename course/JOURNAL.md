# Build journal

Plain English, day by day, including the parts that went wrong. Drafted by Claude from the working sessions, edited by Subhasish. Where it says a mistake was made, that is not modesty, it is the record.

The status file is `course/STATE.md`. This file is the story.

---

## 18th to 19th September. Starting from genuinely nothing.

The plan was a bot that triages GitHub issues. The honest starting point: I did not know what a repository, an issue or a maintainer meant in this context. What landed first was the analogy. The repo is the product, an issue is a support ticket, the person who reported it is the customer, the maintainer is second line support and product owner in one person, and the bot is first line.

Named it **FirstPass**. Wrote the first brain dump: what it should never do, what a good demo looks like, what scared me. On "which repo should we test on" the honest answer was "no idea". On "biggest fear" it was "escalating everything is better than being confidently wrong in public".

That last line turned out to be the whole product.

## 20th September. The name was already taken, by a bank.

Checked the name before building anything. **FirstPass is First Financial Bank's voice biometrics login.** Also found that Chatwoot's free plan had dropped API and webhook access in July, which would have blocked the build at module six.

Both of those would have been expensive to discover later. Checking names and dependencies before writing code is now a habit rather than a step.

## 21st September. The market said no.

Ran the competitive work. Two findings killed the original idea.

GitHub had shipped its own agentic workflows with code-enforced write limits, which is the safety pattern the product was going to be built around. And **Dosu, the best known AI triage bot for open source, left issue triage in August 2026.** The category leader walked away.

The question that mattered: if the segment is being absorbed by the platform, what sense does it make to spend a month proving how often a bot in that segment is wrong?

## 21st to 22nd September. Pivot to bank complaints.

Same machinery, different domain: an AI support agent for a fictional bank, where getting the handoff wrong has legal consequences rather than social ones. Fourteen years in fintech is an actual edge here, which it never was in open source tooling.

The agent became **Warmhand**, from warm handoff. The bank became **Kettlewick**, fictional and obviously so. Forty six things had to change and they were worked through in two passes rather than one.

## 22nd September. Reading other people's code, and finding my own bug.

Pulled six applications from a public collection of agent examples and read them line by line. Three patterns were worth stealing, and one of them upgraded the product: **a citation must quote the source, and the quote must be checked in code against the actual text.** A model can cite the right document and still invent what it says.

Then a review of the PRD found a bug I had introduced myself. The relevance gate I had added would skip the model entirely when no help article matched, which meant a paraphrased scam message would get a generic reply instead of a crisis handoff. Fixed the same day: classification always runs, and the gate applies only to the answering step.

A safety feature that made the product less safe. Worth remembering.

## 24th September, morning. Nearly published my interview details.

Before the first commit, scanned the files for anything that should not be public and found the name of a company I was interviewing with, the round structure, and a former employer's name. Cleaned all of it.

Then the other Claude window asked one question that changed the day: **had anyone checked git history, or only the working files?**

Only the working files. A commit already existed from module zero, and it still contained every line that had just been removed. `git push` sends the whole album, not the latest photo. Pushing would have published exactly what the cleanup was for.

Because nothing had left the laptop yet, the first commit could be amended in place. It was, and the repository went public clean.

**The rule that came out of it:** for a public repo, scan history, not the working tree. A working tree scan misses everything already committed.

## 24th September, afternoon. A federal agency deleted the data source.

The evaluation set was going to be built from the CFPB's public complaint database. The API returned no complaint text. Checked three ways: the website export, the full database download, the public API. All fifteen columns, no narrative anywhere.

**The CFPB stopped publishing consumer complaint narratives on 14th August 2026**, six weeks before we looked. Their stated reasons: discretionary, unverified, one sided.

The narratives published before that date were not withdrawn. They were moved to the Bureau's FOIA reading room as bulk downloads. So the data exists, it is finite, and it will never grow again.

That made the dataset more valuable, not less. Nobody can generate a new one.

## 24th September, later. I made up a number.

Writing this up, I stated that narratives were published "after the company responds or 60 days, whichever is earlier". The other window asked for the source. There was not one. The figure had come from a summary of a page rather than from the page.

The real rule, quoted from the CFPB's own site, is 15 days, and it is about complaints rather than narratives specifically.

Second near miss in one day, same shape both times: a plausible claim treated as verified because it sounded right. **Which is exactly what the product is being built to prevent.** The reason Warmhand checks quoted citations in code, rather than trusting a model to cite honestly, stopped being theoretical.

## 27th September. Measuring instead of guessing.

Wrote the first script. Counted the real pool: **19,569 complaints with text** across credit cards and bank accounts, April to June 2026. Every stratum comfortably supplied.

Excluded July on purpose. The publication cutoff means July's surviving narratives skew toward complaints companies answered quickly, so the slow, badly handled ones are missing. Dropping a third of the data to avoid a bias you could have quietly caveated is the sort of decision worth being able to explain.

One finding nobody expects: **the median complaint is 206 words.** These are written submissions, not chat messages. The evaluation had to be honest about testing triage of a long written complaint.

Drew the gold set, wrote five help articles for the fictional bank, and wrote forty synthetic questions including fifteen deliberate near misses. The sharpest one: "how long do I have to dispute a charge?" It reads like a general policy question. Answering it means quoting a legal deadline, which the policy forbids.

## 28th September. The audit that stopped everything.

Asked for an outside view. The numbers:

| Measure | Value |
|---|---|
| Words of documentation | 39,636 |
| Lines of Python | 347, all data wrangling |
| Calls to a model | 0 |
| Days elapsed | 10 |

Ten days building an agent, and nothing in the repository was an agent. Every "carry on" had produced another document, because documents are the fastest thing to produce and they feel like progress.

The audit also named something worse. **The evaluation is circular.** The policy author is the label author, the bank is fictional, the articles are invented. A perfect score measures compliance with the policy, not whether the policy is any good.

Same day: gold set cut from 120 cases to 30 so the loop closes in one sitting, a README written that states the circularity before a reviewer can find it, a brief drafted for a second labeller with real bank operations experience, and all feature work frozen until a model call exists.

## 30th September. The first API call.

Two files, about thirty lines, typed rather than pasted. The first said hello. The second read a real CFPB complaint and classified it.

Twelve days in, this project finally spoke to a model.

**Cost, measured rather than assumed:** about $0.00057 for one classification, roughly $18 a month at ten thousand complaints. Cost is not a constraint on this product at any plausible volume, which means every model decision from here is about quality, not price.

**The finding that mattered more.** The model answered `hand_off` on a credit report dispute. That is correct under the policy, which treats credit report errors as a legal clock. But the prompt said nothing about credit reports, or FCRA, or legal clocks. It got the right answer because the word "dispute" happened to be vague enough to cover it.

A prompt that produces the right answer for the wrong reason is not a control. That is module two's job, and it is the difference between a script and an agent.

---

## What this journal is for

Three things get lost if this is not written down.

The **near misses**, all three of them, are worth more than the successes. Interview details nearly published because history was not scanned. A number invented and nearly committed. A safety feature that made the product less safe. Each one was caught by a check rather than by luck, and each one is now a rule.

The **honest ratio**. Ten days of documents before a single model call. That is a real failure of judgement, it has a named cause, and it was fixed by cutting scope rather than by working harder.

The **decisions with reasons attached.** Why the name changed. Why the domain changed. Why July was dropped. Why the gold set is 30 and not 120. Six months from now the decisions will look obvious and the reasoning will be gone, which is how projects quietly lose the plot.
