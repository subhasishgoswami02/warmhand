# Module 0B: going public safely

**What this is.** The four Module 0 gaps, closed in order: a hook that blocks `.env` from ever being committed, the MIT license, three clean commits, and the public GitHub repo. About 30 to 40 minutes. **You type everything, in your Mac terminal or in Claude Code.** Ask Claude Code to explain any command before you run it.

**Why now.** More than 20 files of product work exist only on your laptop, uncommitted. A dead disk loses all of it. The project rule is also "public from commit one", and today nothing is public.

---

## Step 1. Pre-flight check

**Why.** Confirm the one thing that must never happen hasn't already.

```bash
cd ~/Developer/triage-agent
git status
git check-ignore -v .env
git ls-files | grep -i env
```

**Expect:** `git check-ignore` names the `.gitignore` line that ignores `.env`. `git ls-files` shows only `.env.example`. If `.env` appears in `git ls-files`, **stop** and tell Claude Code before doing anything else.

## Step 2. A pre-commit hook that blocks `.env`

**Concept.** A git hook is a small script git runs at a set moment. A **pre-commit** hook runs just before every commit. If it exits with an error, the commit is refused.

**Why, when `.gitignore` exists already?** `.gitignore` only stops *accidental* adds. It does nothing against `git add -f .env`, a renamed copy like `.env.local`, or a tool that stages everything. The hook is a second net, and it protects your own commits too, not only Claude Code's.

**Build it (you type it, Claude Code can explain each line):**
1. Create a folder `.githooks/` and a file `.githooks/pre-commit` inside it
2. The script's logic, in plain words: *list the files staged for this commit* (`git diff --cached --name-only`). *If any name is `.env`, or starts with `.env.` but isn't `.env.example`, print a clear warning and exit with 1. Otherwise exit with 0*
3. Make it executable: `chmod +x .githooks/pre-commit`
4. Tell git to use this folder for hooks: `git config core.hooksPath .githooks`

**Why a `.githooks/` folder and not `.git/hooks/`?** Files inside `.git/` are never committed. A hook in `.githooks/` lives in the repo, so anyone who clones it gets the same protection after running step 4.

**Proof:**
```bash
git add -f .env
git commit -m "test"        # must be REFUSED with your warning
git restore --staged .env   # unstage it again
git status                  # .env must not be listed
```

**Optional, a Claude Code guard:** add a deny rule in `.claude/settings.json` so Claude Code can never *read* `.env`: `{"permissions": {"deny": ["Read(./.env)"]}}`. Ask Claude Code to confirm the current syntax before relying on it. The git hook guards commits. This guards the file from the AI itself.

## Step 3. The MIT license

**Concept.** A license tells strangers what they may do with your code. MIT means anyone may use, copy and change it, as long as they keep your copyright notice, and you give no warranty. It's the most common license for open source portfolio work.

**Build:** create a file named `LICENSE` in the repo root. Copy the MIT text from https://choosealicense.com/licenses/mit/ and fill in `Copyright (c) 2026 Subhasish Goswami`.

**Why locally, not by ticking "add a license" on GitHub?** Ticking it makes GitHub create a first commit on its side. Then your local history and GitHub's history start differently, and the first push is refused. Keep GitHub empty and bring everything from your laptop.

## Step 4. Three commits, so the story is readable

**Concept.** Small commits with clear messages make the history a record of how you think. The pivot should be visible: GitHub era work first, then the pivot.

Before **every** commit, check exactly what's staged:
```bash
git status
git diff --cached --name-only
```
`references/` must never appear. It's gitignored, because it's someone else's code.

**Commit A: the pre-pivot evidence**
```bash
git add docs/archive/
git commit -m "Archive GitHub-era PRD and competitive brief (evidence for the pivot)"
```

**Commit B: safety and license**
```bash
git add LICENSE .githooks/
git commit -m "Add MIT license and a pre-commit hook that blocks .env files"
```

**Commit C: the pivot**
```bash
git add .gitignore .env.example brain_dump.md prd.md course/ docs/
git commit -m "Pivot to bank complaint triage: Warmhand PRD v1.3, escalation policy, research"
```

**Proof:** `git log --oneline` shows four commits (Module 0 plus A, B, C).

## Step 5. Create the public repo and push

**Concepts.** A **remote** is a copy of your repo on another machine, here GitHub. **origin** is the conventional name for your main remote. **Push** sends your commits there. `-u` sets it as the default, so later you just type `git push`.

**Name:** `warmhand` on GitHub. Your local folder stays `triage-agent`, and that's fine.

**Option 1, the GitHub website:** go to github.com/new. Name `warmhand`, **Public**, and **leave "Add a README", ".gitignore" and "license" all unticked**. Then:
```bash
git remote add origin https://github.com/<your-username>/warmhand.git
git branch -M main
git push -u origin main
```

**Option 2, the GitHub CLI** (if `gh --version` works): `gh auth login`, then `gh repo create warmhand --public --source=. --remote=origin --push`

**Authentication:** GitHub doesn't accept your account password for git over HTTPS. Use `gh auth login`, or a personal access token when prompted.

## Step 6. Turn on GitHub's secret push protection

**Why.** A third net: GitHub scans every push for things that look like API keys and blocks them. It's free for public repos.

**How:** on the repo page, go to **Settings**, then **Code security**, and enable secret scanning and push protection. The menu wording changes over time, so ask Claude Code if you can't find it.

## Step 7. Verify, in public

- On GitHub, the file list shows `LICENSE`, `.env.example`, `prd.md`, `course/`, `docs/`, and **no `.env` and no `references/`**
- `git status` says "Your branch is up to date with 'origin/main'"

## Step 8. Explain it back, in Claude Code

Three sentences each, in your own words. Claude Code records the answers in STATE.md and doesn't accept "it worked":

1. What does a virtual environment protect you from?
2. Why is `.env.example` committed but `.env` is not?
3. If you commit an API key and delete it in the very next commit, is the key safe? Why not?
4. **New:** what does the pre-commit hook protect you from that `.gitignore` doesn't?

**Module 0 is done** when all eight steps pass and the four answers are clear.
