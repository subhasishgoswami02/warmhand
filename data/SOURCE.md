# Where the raw data came from

(This file is committed. The data it describes is not. `.gitignore` excludes `data/raw/`.)

## The constraint that shapes everything below

**The CFPB stopped publishing consumer complaint narratives on 14th August 2026.** Announced that day, effective immediately. Its stated reasons: the narratives are discretionary, unverified, present one side of an issue, and publishing them risks misleading consumers and harming company reputations. Complaints are still collected and the structured fields are still published. Only the consumer's own text is gone.

Announcement: https://www.consumerfinance.gov/about-us/newsroom/the-cfpb-to-cease-discretionary-publication-of-complaint-narratives-and-visualizations/

Narratives published before that date were **not** withdrawn. They remain in the public domain and the CFPB moved them to its FOIA Reading Room. A pre-August-2026 snapshot is therefore legitimate public data, not a workaround, provided its date is stated.

Verified independently on 24th September 2026, three ways, all agreeing: the website's filtered CSV export, the full database download, and the public API all return 15 columns with no narrative field.

## Two sources, two jobs

### 1. Current structured data, for counts and category weights

`data/raw/complaints.csv.zip`, the full database export, downloaded 24th September 2026. About 347MB zipped, 5.4GB unzipped. Read from the zip in chunks; it is not unzipped.

Columns: Date received, Product, Sub-product, Issue, Sub-issue, Company public response, Company, State, ZIP code, Tags, Submitted via, Date sent to company, Company response to consumer, Timely response?, Complaint ID.

No narrative. This file answers how many, of what kind, tagged how. It cannot supply a single test case.

`data/raw/cfpb_ui_export_crosscheck.csv`, 12MB, the website's filtered export for credit card and checking or savings, 23rd June to 23rd September 2026. Same 15 columns. Its only job is verification: filtering the full database in code must reproduce it exactly, by row count and by complaint ID.

| Check | Expected |
|---|---|
| Total rows | 42,847 |
| Credit card | 21,693 |
| Checking or savings account | 21,154 |

If the code filter does not match, the filter is wrong, not the file.

Search URL that produced it:

https://www.consumerfinance.gov/data-research/consumer-complaints/search/?dateRange=3m&date_received_max=2026-09-23&date_received_min=2026-06-23&page=1&product=Checking%20or%20savings%20account&product=Credit%20card&searchField=all&size=25&sort=created_date_desc

### 2. Historical narratives, for the escalation half of the gold set

TO BE FILLED IN when the snapshot is obtained. Must record: where it came from, its snapshot date, how it was verified as genuine CFPB data, and its row count. Prefer the CFPB's own FOIA Reading Room over a third-party mirror. A mirror is acceptable for public-domain government data but its provenance and snapshot date must be stated, and a sample of its complaint IDs must be checked against the current database to confirm the records are real.

The README states plainly that narratives are historical and why. It never implies the set is live.

## The gold set design that follows

| Half | Source | Why |
|---|---|---|
| Escalation cases | Historical narratives, pre-14th August 2026 | Real consumer text, real categories, no longer reproducible by anyone |
| Answerable cases | Written by hand from the help articles | A regulator complaint corpus contains no easy questions, by construction |
| Category weights | Current structured data, this month | So the mix reflects what banks actually receive now, not 2026 history |

The committed gold set is complaint ID plus our labels, never the narrative text. Labels are ours; the text is CFPB's. Pinning by ID keeps the set reproducible and keeps consumer text out of this repo.

## Caveats that shape the product, not just the data handling

1. Narratives arrive pre-redacted, with personal details replaced by `XXXX`. They cannot test the PII masker. The masker needs its own synthetic recall and precision sets.
2. This is a post-failure corpus. Everyone in it already went to their bank and escalated to a federal regulator, so it contains almost no answerable questions. Evaluating only on it would reward an agent that escalates everything.
3. Consumers who consented to publication are not a random sample of complainants. The README says so rather than implying the set is representative.
4. The narrative corpus is now closed. It will not grow, and it ages. Any claim about current complaint language must come from the structured data, not the narratives.

## Number discipline

The website showed two different totals for "total complaints" on two different views. No number from the web page goes into the README or any post. Every published figure is computed from these files by a script in this repo.
