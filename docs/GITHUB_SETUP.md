# GitHub setup notes (PAT + push)

## What you need
- Git installed (if `git --version` fails, install from the official Git website)
- A GitHub account
- A GitHub repository created for your assessment

## Configure Git (local machine)
Open the terminal in VS Code and run:
```bash
git config --global user.name "mnikita231"
git config --global user.email "munjalnikita11@gmail.com"
```

## Create a Personal Access Token (PAT)
GitHub no longer accepts account passwords for Git operations over HTTPS. Use a PAT instead:

1. GitHub → your profile icon → **Settings**
2. **Developer settings**
3. **Personal access tokens** → choose the right token type for your course (often “Tokens (classic)” is simplest)
4. Generate a token and copy it somewhere safe (you may not see it again)

When Git prompts for a password during `git push`, paste the PAT.

## Push workflow (typical)
From inside your project folder:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <YOUR_GITHUB_REPO_URL>
git branch -M main
git push -u origin main
```

## Verify
Open your GitHub repository page and confirm the files appear in the repo.
