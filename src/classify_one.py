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
print("CFPB issue:", case["Issue"])
print("Words:", case["narrative_words"])
print("-" * 60)

prompt = f"""Triage this bank complaint.

Reply with exactly one word: answer, hand_off, or crisis.

answer = a general policy question a help article could answer
hand_off = a specific account, a dispute, money movement, or a vulnerable customer
crisis = distress, self harm, or a scam in progress

Complaint:
{complaint}"""

start = time.time()
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=10,
    messages=[{"role": "user", "content": prompt}],
)
elapsed = time.time() - start

print("Model said:", response.content[0].text.strip())
print("Tokens in", response.usage.input_tokens, "out", response.usage.output_tokens)
print(f"Took {elapsed:.1f} seconds")
