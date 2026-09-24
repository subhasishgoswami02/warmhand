# Brain dump

Raw Stage 1 answers, 18th to 19th September 2026. Kept as said, with one change for the public repo: a reference to a specific company I was comparing against is removed.

**Where I started.** I did not know what a GitHub repo, an issue or a maintainer meant in this context. What landed: the repo is the product, an issue is a support ticket, the reporter is the customer, the maintainer is L2 plus product owner in one person, and the bot is L1.

**Why this and not something else.** Honestly, it was suggested because it is close to support deflection work I have shipped before, and to what an AI company I admire has done. I just wanted an end to end building experience.

**Name.** I liked either "the job" or "the role" as a direction. My worry about FirstPass: it gives no indication of the actual work or where it happens. Resolved by pairing it with a descriptor line rather than a literal name.

**One sentence.** FirstPass does the first pass on every new GitHub issue, labeling it and answering from the project's own docs, and hands it to a maintainer when it can't cite an answer or the call isn't its to make.

**What it should never do.** Delete, approve critical flows probably. Kept a list of seven and asked for each to be pressure-tested. Example of the worry: "reply twice to the same issue". The user can have a genuine reply, won't you reply again?

**Which repo to test on.** No idea.

**The demo that would make me proud.** Something that works, and showcases the escalation matrix probably. Not sure.

**Biggest fear.** Escalates everything is better to start with than confidently being wrong in public. Better safe than sorry. Also, it shouldn't be manipulated.

---

# Pivot brain dump: bank complaint triage (20th September 2026)

**Drafted by Claude at Subhasish's request**, from general public industry knowledge. No employer data. Subhasish reviews and edits. Anything he changes is his judgment, and it wins.

**Why the switch, in his words.** "If this segment or area itself doesn't make sense anymore, what sense does sticking to it and proving and publishing how often the bot is wrong make?"

**Names.** He wanted a Harry Potter theme. Franchise names are trademarked (Gringotts is registered by Warner Bros), so the bank carries the flavor (**Kettlewick Bank**, fictional) and the agent carries the positioning (**Warmhand**, from "warm handoff").

**What a bank bot must never touch**
- Moving money of any kind: refunds, reversals, credits, fee waivers, payments, transfers
- Account data: balances, transactions, statements. It has no access and must never pretend it does
- Identity: never asks for or repeats a full card number, CVV, PIN, one time code, password or Social Security number. A bank bot asking for these looks exactly like phishing
- Credit decisions: why an application was denied, credit limit changes. Denial reasons are regulated
- Legal, tax or investment advice
- Anyone who may not be the account holder ("I'm calling for my mother", "my husband's card")

**Complaints with a legal clock** (US rules, summarized for a fictional US bank. Verify before publishing. Not legal advice)
- Unauthorized debit card or electronic transfer (Regulation E): how much the customer can lose depends on how fast they report it, so any delay by the bot can cost them money. The bank has to investigate on a fixed timeline
- Disputed credit card charge or billing error (Regulation Z): written dispute within 60 days of the statement, then acknowledgement and resolution deadlines for the issuer
- Unauthorized credit card use: customer liability is capped by law
- Credit report errors (FCRA): investigation deadlines, usually 30 days
- A complaint lodged through the CFPB: the company has response deadlines
- Servicemembers (SCRA): special protections, including an interest rate cap on debt taken on before service
- Bankruptcy: collection must stop
- Discrimination claims (ECOA, Regulation B)

**What a vulnerable customer sounds like**
- Bereavement: "my husband passed", "I'm handling my mother's account"
- Illness, hospital stays, disability, confusion
- Job loss, can't pay, choosing between bills
- Scam victims: "I sent money to someone who said he was from the bank"
- Financial or domestic abuse: "my partner controls the account", "cards opened in my name"
- Older customers lost in digital banking
- Distress or crisis language, including any mention of self harm: straight to a human, never automated advice
- Language barriers

Rule of thumb: if you're unsure whether someone is vulnerable, treat them as vulnerable. A false positive costs one human conversation.

**Words that force a handoff whatever the topic.** Lawyer, attorney, sue, lawsuit, CFPB, regulator, attorney general, BBB, news, media, discrimination, fraud, scam, stolen, identity theft, didn't authorize, dispute, bankrupt, passed away, deceased, military, deployed. **A keyword list is a floor, not the classifier.** Code catches the words. The model catches the paraphrases. Either one is enough to hand off.

**What the bot can safely do**
- Explain general policy from the help articles, with a citation (how disputes work, the fee schedule, how to freeze a card in the app)
- In a fraud report, tell the customer how to freeze their card in the app. That's protective, not a promise
- Ask for missing details that aren't sensitive (which product, what happened in one line)
- Hand off with a note, so the customer never has to repeat themselves

**What scares me**
- The bot explains a dispute deadline wrongly and the customer misses it
- The bot "reassures": "you won't be liable" is a promise
- The bot asks for a card number
- A scam victim gets a cheerful FAQ answer
- Someone pretending to be the account holder
