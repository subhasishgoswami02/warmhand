# How to label the gold set

120 cases in `evals/gold_set_raw.csv` (local only, never committed). Your labels are the asset in this repo. Anyone can download the CFPB data. Nobody else has a bank product manager's escalation calls attached to it.

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

1. **Label on content, not on length.** 17 of the 120 are over 400 words and would hand off on length alone under policy v0.3. Label them as if that rule did not exist. That way we can measure whether the length rule agrees with the content rule, rather than baking the answer in.
2. **Do not let any model label for you.** A benchmark of one model against another model's opinion measures nothing. Every one of the 120 is your call.
3. **Label blind to the stratum column** where you can. Knowing a case was drawn as "reg_e_unauthorized" will pull you toward handing off. Read the narrative first, decide, then look.
4. **Expect to disagree with yourself.** Note the ones you found hard. Relabel the whole set a week later if you want a consistency check. Disagreeing with your past self on 5 of 120 is a real and publishable number, and a more honest one than claiming perfect consistency.
5. **`answer` should not be zero, but it will be rare.** This is a regulator complaint corpus: everyone in it already tried their bank. If you end up with two or three `answer` cases out of 120, that is the data telling the truth, and it is exactly why the synthetic answerable half exists.

## Budget

Two to three hours. Do it in two sittings rather than one, and do not do it tired. The point of this file is decisions you would defend in front of a compliance officer.

## When you finish

The narrative text stays local. The committed file is complaint ID plus your three label columns plus the metadata, so anyone can rehydrate the text from the CFPB archive and check your calls.
