# Module 0: Foundations

## Why this module exists

Every leaked API key in history came from someone who skipped this and planned to tidy up later. Git remembers deleted files. A key committed once and removed in the next commit is still public forever.

You are also building the thing you will show people. The repo starts clean or it never is.

## Concepts

**Virtual environment.** Your Mac has a system Python that macOS itself depends on. Installing packages into it breaks things and makes your project impossible for anyone else to reproduce. A venv is a private Python for this project only. `requirements.txt` records exactly what is in it.

**Environment variables.** Secrets live outside the code, in a `.env` file that is never committed. The code reads them at runtime. `.env.example` is committed, with the names but no values, so someone else knows what to supply.

**.gitignore.** A list of things git must never track. `.env` is on it before `.env` exists. That order matters.

**Commit hygiene.** Small commits with real messages. Your git history is a record of how you think.

## Build

Run these in your own Mac Terminal, not anywhere else.

```bash
cd ~/Developer/triage-agent
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
git init
git add .gitignore .env.example course/
git commit -m "Module 0: repo skeleton, secret hygiene, course plan"
cp .env.example .env
git status
```

## Proof

- `git status` shows `.env` is NOT listed as untracked. If it appears, `.gitignore` is wrong and you stop and fix it before anything else.
- `which python` points inside `.venv`.
- `git log --oneline` shows exactly one commit.

## Explain it back

In your own words, in three sentences each:

1. What a virtual environment protects you from.
2. Why `.env.example` is committed and `.env` is not.
3. What happens if you commit a key and then delete it in the next commit.
