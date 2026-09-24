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

### 2. Archived narratives, for the escalation half of the gold set

Source: the CFPB's own FOIA Electronic Reading Room, **CFPB Consumer Complaint Database Narratives Archive**.

https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/

Direct bulk download, no request or approval process. It holds complaints received 1st December 2011 through 14th August 2026 that were previously published in the Consumer Complaint Database, split into 21 ZIP exports. Recent periods are released monthly; older ones cover multi-month or multi-year ranges.

Taken from the CFPB directly rather than a third-party mirror, so provenance is not in question.

Direct file URLs, taken from the archive page on 24th September 2026:

- April 2026: https://files.consumerfinance.gov/f/documents/CCDB_Export_17_April_2026.zip
- May 2026: https://files.consumerfinance.gov/f/documents/CCDB_Export_18_May_2026.zip
- June 2026: https://files.consumerfinance.gov/f/documents/CCDB_Export_19_June_2026.zip
- July 2026: https://files.consumerfinance.gov/f/documents/CCDB_Export_20_July_2026.zip
- August 2026: https://files.consumerfinance.gov/f/documents/CCDB_Export_21_August_2026.zip

**Exports downloaded: April through August 2026.** The current structured data window is 23rd June to 23rd September 2026 and the narrative archive ends on 14th August 2026, so the two overlap. April through June is the primary pool for test cases, July is supplementary, August carries none. Reasoning below.

If a stratum turns out too thin, the archive reaches back through March 2026 (`CCDB_Export_16_March_2026.zip`), then two-month and multi-year exports to December 2011.

Downloaded 24th September 2026 (files uploaded by the CFPB on 14th September 2026). Each export covers one calendar month and carries 16 columns: the same 15 as the current database plus `Consumer complaint narrative`.

| Export | Rows | Rows with narrative | Credit card + checking, with narrative |
|---|---|---|---|
| April 2026 | 618,293 | 21,052 | 7,380 |
| May 2026 | 619,940 | 17,528 | 6,079 |
| June 2026 | 620,794 | 16,820 | 6,110 |
| July 2026 | 672,036 | 10,002 | 3,847 |
| August 2026 | 667,140 | 1 | 0 |

Usable pool: **23,416** credit card and checking or savings complaints with narrative text, dated 1st April to 31st July 2026.

**A publication lag truncates the last two months.** The CFPB publishes a complaint "after the company responds or after 15 days, whichever comes first" (https://www.consumerfinance.gov/complaint/data-use/). Publication ceased entirely on 14th August 2026, so complaints received close to that date, and all complaints received after it, never reached publication.

We have not found a published figure for how long a narrative specifically took to appear, as distinct from the complaint record, so no interval is claimed here beyond the sourced 15 days. The effect is visible in the counts regardless, and the counts are our own.

What the counts show: April 7,380, May 6,079, June 6,110, July 3,847, August 0. April is highest, May and June are level with each other, and the drop is sharp at July. So this is not a gradual decline from April onward. It bites at July and August.

Two consequences:

1. August carries no test cases at all. It is useful for structured counts only.
2. The July narratives that exist are likely skewed toward complaints the company answered quickly, because an early company response is what triggers earlier publication. Slow-response cases, which are often the mishandled ones, are probably under-represented in July. This is inference from the publication rule plus the observed drop, not a documented fact, and the README says so.

Primary pool for the gold set: **April, May and June 2026**, which are comparable to each other. July is supplementary and flagged in the README. August is excluded from test cases.

April and May exports added for this reason:
- April 2026: https://files.consumerfinance.gov/f/documents/CCDB_Export_17_April_2026.zip
- May 2026: https://files.consumerfinance.gov/f/documents/CCDB_Export_18_May_2026.zip

**Narratives keep real company names.** Personal details are replaced with `XXXX`, but the bank being complained about is named in the text. This is a second reason the repo commits complaint IDs and our labels only, never the text, and why no individual complaint is quoted in the README or any post.

The README states plainly that narratives end on 14th August 2026 and why. It never implies the set is live or growing.

## The gold set design that follows

| Half | Source | Why |
|---|---|---|
| Escalation cases | Historical narratives, pre-14th August 2026 | Real consumer text, real categories, no longer reproducible by anyone |
| Answerable cases | Written by hand from the help articles | A regulator complaint corpus contains no easy questions, by construction |
| Category weights | Current structured data, this month | So the mix reflects what banks actually receive now, not the pre-August snapshot |

The committed gold set is complaint ID plus our labels, never the narrative text. Labels are ours; the text is CFPB's. Pinning by ID keeps the set reproducible and keeps consumer text out of this repo.

## Caveats that shape the product, not just the data handling

1. Narratives arrive pre-redacted, with personal details replaced by `XXXX`. They cannot test the PII masker. The masker needs its own synthetic recall and precision sets.
2. This is a post-failure corpus. Everyone in it already went to their bank and escalated to a federal regulator, so it contains almost no answerable questions. Evaluating only on it would reward an agent that escalates everything.
3. Consumers who consented to publication are not a random sample of complainants. The README says so rather than implying the set is representative.
4. The narrative corpus is now closed. It will not grow, and it ages. Any claim about current complaint language must come from the structured data, not the narratives.

## Number discipline

The website showed two different totals for "total complaints" on two different views. No number from the web page goes into the README or any post. Every published figure is computed from these files by a script in this repo.
