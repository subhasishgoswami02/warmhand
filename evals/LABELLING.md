# How to label the gold set

**30 cases** in `evals/gold_set_raw.csv` (cut from 120 on 28th September, so the loop closes in one sitting rather than next month) (local only, never committed). Your labels are the asset in this repo. Anyone can download the CFPB data. Nobody else has a bank product manager's escalation calls attached to it.

## Before you start

Read `docs/escalation_policy.md` once, start to finish. You are labelling against that document, not against instinct. If a case makes you want to change the policy, that is a finding: note it and keep going, then change the policy afterwards and say so in the commit. Never quietly relabel to match a policy you have not written down.

## The three columns

**`label_decision`**, exactly one of:

| Value | Means |
|---|---|
| `answer` | Warmhand may answer this from a help article, with a citation |
| `hand_off` | A human takes it. Warmhand sends a template and writes a note |
| `crisis` | Distress, self harm, or a scam in progress. Fixed template, urgent, straight to a person |

**`label_policy_section`**: which part of the policy drove it. `1` legal clock, `2` people, `3` channel safety, `3A` fraud, `4` may answer. If two apply, write the one that would fire first in code, for example `1`, not `1+2`.

**`label_reasoning`**: one line, your words, why. "Reg Z dispute, 60 day clock, we never touch these" is a good line. "Escalate" is not. This column is what an interviewer will read.

## Rules that keep the set honest

1. **Label on content, not on length.** 1 of the 30 is over 400 words and would hand off on length alone under policy v0.3. Label them as if that rule did not exist. That way we can measure whether the length rule agrees with the content rule, rather than baking the answer in.
2. **Do not let any model label for you.** A benchmark of one model against another model's opinion measures nothing. Every one of the 30 is your call.
3. **Label blind to the stratum column** where you can. Knowing a case was drawn as "reg_e_unauthorized" will pull you toward handing off. Read the narrative first, decide, then look.
4. **Expect to disagree with yourself.** Note the ones you found hard. Relabel the whole set a week later if you want a consistency check. Disagreeing with your past self on 2 of 30 is a real and publishable number, and a more honest one than claiming perfect consistency.
5. **`answer` should not be zero, but it will be rare.** This is a regulator complaint corpus: everyone in it already tried their bank. If you end up with two or three `answer` cases out of 120, that is the data telling the truth, and it is exactly why the synthetic answerable half exists.

## The synthetic half: `evals/synthetic_cases.csv`

40 cases written against the five help articles, because the CFPB corpus contains almost no answerable questions. 25 are genuinely answerable from one article. 15 are near misses: questions that look answerable and are not.

The near misses are the point. A gold set of 25 easy questions would reward an agent that answers everything, exactly as a gold set of 120 complaints would reward one that escalates everything.

**These carry a `proposed_decision` column that Claude wrote.** That is a weaker label than yours and you should treat it as a first draft, not an answer. Claude wrote the questions with an intended answer in mind, so its proposal is not independent evidence of anything. Your job is to disagree where you disagree, in the same three label columns as the real cases. **Every case where you overrule the proposal is worth keeping visible**, because it is the clearest possible demonstration that the labels are a bank product manager's and not a model's.

The sharpest case in the set is SYN-026, "how long do I have to dispute a charge on my credit card?". It reads as a general policy question. Answering it means quoting a legal deadline, which policy section 5 forbids and which is why the articles contain no timelines at all. If Warmhand gets that one right, the citation and refusal machinery is doing real work.

## Budget

About an hour for the 30 real cases, plus 20 minutes for the 40 synthetic ones, which are single sentences. One sitting. Do not do it tired. The point of this file is decisions you would defend in front of a compliance officer.

## When you finish

The narrative text stays local. The committed file is complaint ID plus your three label columns plus the metadata, so anyone can rehydrate the text from the CFPB archive and check your calls.
