# Module 1: the first API call

**Why this module is now the only thing that matters.** On 28th September an audit of this repo found 39,636 words of documentation, 347 lines of data wrangling, and zero calls to a language model. Ten days in, nothing here is an agent. This module fixes that in about 45 minutes and roughly 30 lines of code that you type.

Nothing else gets added to this repo until this runs.

---

## Concept 1: what an API call actually is

An API call is a letter. You send a package of text to a computer somewhere else, it sends a package of text back, and the connection closes. There is no ongoing conversation and nothing is remembered. If you want the model to know what was said before, you send that too, every time.

That single fact explains most of what looks strange about building with models later: why conversations get expensive as they get longer, why "memory" has to be built rather than assumed, and why an agent is mostly plumbing around a stateless function.

## Concept 2: the key, and why it lives in .env

The key is a password that says the bill goes to you. Anyone holding it can spend your money. That is why it goes in `.env`, why `.env` is in `.gitignore`, and why the pre-commit hook refuses to stage it. You explained this back correctly in Module 0. Now it becomes real, because from today the key is worth something.

## Concept 3: tokens

The model does not see words, it sees tokens: chunks of roughly four characters. You are billed per token in and per token out, at different rates. A 206-word complaint is roughly 270 tokens. Knowing the count is how you answer "what does this cost at ten thousand complaints a month", which is a question you will be asked.

---

## Step 1. Install the two libraries

```bash
cd ~/Developer/triage-agent
source .venv/bin/activate
pip install anthropic python-dotenv
```

`anthropic` sends the letter. `python-dotenv` reads your `.env` file so the key never appears in your code.

## Step 2. Put the key in .env

Open `.env` in Cursor or any editor. It already has the variable name waiting:

```
ANTHROPIC_API_KEY=sk-ant-...
```

Paste your real key after the equals sign, no quotes, no spaces. Save.

Now prove it is loaded and, just as importantly, that it is not about to be committed:

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); k=os.getenv('ANTHROPIC_API_KEY'); print('loaded, ends', k[-4:] if k else 'NOTHING')"
git status --short
```

The first prints the last four characters. The second must not list `.env`. If it does, stop and fix `.gitignore` before anything else.

## Step 3. The smallest call that exists

Create `src/first_call.py`. Type it, do not paste.

```python
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in exactly five words."}],
)

print(response.content[0].text)
print("tokens in:", response.usage.input_tokens)
print("tokens out:", response.usage.output_tokens)
```

Run it:

```bash
python src/first_call.py
```

Five words come back, plus two numbers. **That is the first time this project has touched a model.** Everything from here is that call with better inputs and checks around it.

Read the error if it fails. `authentication_error` means the key is wrong. `not_found_error` on the model name means that model string is wrong, so check the current model names in Anthropic's docs and use one you have access to.

## Step 4. Feed it a real complaint

Now `src/classify_one.py`. Still typed.

```python
import os
import time
import pandas as pd
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

df = pd.read_csv("evals/gold_set_raw.csv")
case = df.iloc[0]
complaint = case["Consumer complaint narrative"]

print("Complaint ID:", case["Complaint ID"])
print("Issue as CFPB labelled it:", case["Issue"])
print("Words:", case["narrative_words"])
print("-" * 60)

prompt = f"""You are triaging a complaint for a bank's support team.

Reply with exactly one word, one of: answer, hand_off, crisis.

answer   = a general policy question a help article could answer
hand_off = anything about a specific account, a dispute, money movement, or a
           vulnerable customer
crisis   = distress, self harm, or a scam in progress

Complaint:
{complaint}"""

start = time.time()
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=10,
    messages=[{"role": "user", "content": prompt}],
)
elapsed = time.time() - start

print("Model said:", response.content[0].text.strip())
print(f"Tokens in {response.usage.input_tokens}, out {response.usage.output_tokens}")
print(f"Took {elapsed:.1f} seconds")
```

## Step 5. Look at what came back

Do not move on until you have actually read it. Ask yourself three things.

**Do you agree with the model?** You have not labelled this case yet, so form your own view first, then compare. Where you disagree is the interesting part and it is the whole reason the gold set exists.

**How much did that cost?** Take the token counts and Anthropic's current published prices and work it out. Then multiply by 30 for the gold set, and by however many runs you expect. Write the number in `course/STATE.md`. An agent whose cost you cannot state is not ready for anybody's production.

**How long did it take?** Compare it to the two minute target in the PRD.

---

## Proof this module is done

1. `src/first_call.py` runs and prints five words plus token counts
2. `src/classify_one.py` runs and prints a one word classification of a real CFPB complaint
3. `git status` does not list `.env`
4. The cost per complaint is written into `course/STATE.md`

## Explain it back, in your own words

1. Why does the model need the whole conversation sent to it every time?
2. What is a token, and why are you billed differently for input and output?
3. The prompt in step 4 tells the model to reply with one word. What happens if it replies with a sentence instead, and why does that make prompt rules weaker than code rules?
4. Your key is now worth money. Name the three things in this repo that stop it reaching GitHub, and say which of the three is a guarantee rather than a courtesy.

Question 3 is the one that matters. It is the bridge to Module 2.
