# PII masking test sets

Two sets, because a masker fails in two directions and only testing one of them is how you ship a broken one.

| Set | Cases | Asks |
|---|---|---|
| `recall.csv` | 22 | Does anything sensitive survive? |
| `precision.csv` | 18 | Does anything harmless get eaten? |

## Why these are synthetic and not drawn from the CFPB data

The CFPB scrubs personal information before publishing, replacing it with `XXXX`. So the 19,569 real complaints in the gold set pool contain **no unmasked PII at all** and cannot test a masker. Testing on them would produce a perfect score and prove nothing.

That is also why this set is publishable. It contains no real person's data, so it can live in a public repo, and anyone can run it against their own masker.

## Where the values come from

Card numbers are the publicly published test numbers every payment processor uses. They pass the Luhn check and are issued to nobody. Social security numbers use the `999` prefix, which has never been issued. The routing number `987654320` is ABA-checksum valid and unassigned. No value here belongs to anybody.

## The recall set

Each row carries `must_not_appear_in_output`: the exact string that must not survive masking. The test is a substring check on the masked text, not a judgement call.

It covers the formats people actually type, which is the part that breaks simple patterns: spaces every four digits, spaces every two, hyphens, a 15 digit Amex, a number with no label around it, and a card buried 40 words into a long distressed complaint.

## The precision set

Rows that must come through untouched. Dates, dollar amounts, rates, case and order numbers, the last four of a card (which policy allows), and CFPB style `XXXX` and `{$1200.00}` text, which must neither crash the masker nor get masked a second time.

A masker that redacts the dispute date, the amount and the reference number is broken even though it leaked nothing. The human picking up the handoff gets a note with the useful parts blanked out.

## Two open questions, deliberately left in

Both are in `precision.csv` and both need a decision recorded rather than a default:

**PII-P-016**, a 16 digit number that fails the Luhn check. If the masker only masks Luhn-valid numbers, this survives. Is that right? Masking it costs a false positive on a long order number. Not masking it leaks anything mistyped by one digit.

**PII-P-018**, `999 99 9999` used as a rupee amount rather than a social security number. Same digits, different meaning, no way to tell from the pattern alone.

Decide both, write the decision into `docs/escalation_policy.md`, and move the case to whichever set matches the decision. A test set with an undecided case in it is a test set that will be quietly edited later to match whatever the code happened to do.
