#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

echo "📦 Starting Git automation process..."

# 1. Initialize Git if not already done
if [ ! -d ".git" ]; then
    git init
    echo "✅ Initialized empty Git repository."
else
    echo "ℹ️ Git repository already initialized."
fi

# 2. Configure Local Git identity if needed (using your credentials)
git config user.name "Banele477"
git config user.email "banelesomkhanda8@gmail.com"
echo "✅ Git identity configured."

# 3. Create a unified .gitignore to keep the repo clean
cat << 'GITIGNORE' > .gitignore
# Python artifacts
__pycache__/
*.pyc
venv/
.env

# Node.js artifacts
node_modules/
.next/
dist/
out/
build/
.DS_Store
GITIGNORE
echo "✅ Generated .gitignore."

# 4. Stage all created files (backend, frontend, AI module)
git add .
echo "✅ Staged all files."

# 5. Commit changes
git commit -m "Feat: Complete functional scaffolding for AI Disaster Response Assistant" || echo "No changes to commit."

# 6. Ensure default branch is set to 'main'
git branch -M main

# 7. Ask for the remote GitHub URL if not already set
if ! git remote | grep -q "origin"; then
    echo "🔗 Enter your GitHub Repository URL (e.g., https://github.com/Banele477/your-repo-name.git):"
    read -r REPO_URL
    git remote add origin "$REPO_URL"
    echo "✅ Remote origin set to $REPO_URL."
else
    echo "ℹ️ Remote origin is already set."
fi

# 8. Push to GitHub
echo "📤 Pushing code to GitHub..."
git push -u origin main --force

echo "🎉 All files successfully committed and pushed to GitHub!"
