# Assessment Submission Repository (Template)

This folder is a ready-to-zip template you can use for your unit assessment submissions.

## Structure
- `docs/` → Word/PDF write-ups, screenshots, rubrics, references.
- `src/`  → Python code you run in VS Code (scripts, modules).
- `data/` → Any input/output files your code needs (CSV, TXT, etc.).
- `.vscode/` → Optional VS Code settings.

## Quick start (Git + GitHub)
1. Configure Git identity (once per machine):
```bash
git config --global user.name "mnikita231"
git config --global user.email "munjalnikita11@gmail.com"
```

2. Initialize the repo in this folder:
```bash
cd assessment_submission_repo
git init
```

3. First commit:
```bash
git add .
git commit -m "Initial commit - assessment template"
```

4. Create a new GitHub repo (on GitHub website), then link + push:
```bash
git remote add origin <YOUR_GITHUB_REPO_URL>
git branch -M main
git push -u origin main
```

## Notes on authentication
GitHub typically requires a Personal Access Token (PAT) instead of a password for HTTPS pushes.
See `docs/GITHUB_SETUP.md` for the step-by-step.
