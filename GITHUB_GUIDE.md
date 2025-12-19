# GitHub Setup Guide for Task Manager

## 📋 Files to Upload

### ✅ Include These:
```
task-manager/
├── .gitignore          ← Prevents sensitive files from uploading
├── app.py              ← Main application
├── models.py           ← Database models
├── config.py           ← Configuration
├── requirements.txt    ← Dependencies
├── README.md           ← Documentation
├── QUICKSTART.md       ← Setup guide
├── PROJECT_SETUP.md    ← Project info
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    └── tasks.html
```

### ❌ Never Upload These:
- `venv/` - Virtual environment
- `instance/` - Database folder with user data
- `__pycache__/` - Python cache
- `*.db` - Database files
- `.env` - Environment variables

## 🚀 Method 1: GitHub Desktop (Easiest)

### Step 1: Install GitHub Desktop
1. Download from: https://desktop.github.com/
2. Install and sign in with your GitHub account

### Step 2: Create Repository
1. Open GitHub Desktop
2. Click "File" → "Add Local Repository"
3. Click "Create a Repository"
4. Name: `task-manager`
5. Description: "Full-stack task management web application"
6. ✅ Check "Initialize with README" (or use existing)
7. Click "Create Repository"

### Step 3: Commit Files
1. You'll see all your files listed
2. **Important:** Check that `.gitignore` is working
   - You should NOT see: `venv/`, `instance/`, `__pycache__/`
   - If you do see them, don't commit yet!
3. Write commit message: "Initial commit - Task Manager application"
4. Click "Commit to main"

### Step 4: Publish to GitHub
1. Click "Publish repository"
2. ✅ Uncheck "Keep this code private" (unless you want it private)
3. Click "Publish Repository"

**Done!** ✅ Your code is on GitHub!

## 🔧 Method 2: Command Line (Git)

### Step 1: Install Git
If not installed: https://git-scm.com/download/win

### Step 2: Initialize Repository
```bash
cd C:\Users\js_cust_PC2025\documents\portfolio_projects\task-manager

# Initialize git
git init

# Add the .gitignore file first!
git add .gitignore
git commit -m "Add .gitignore"

# Add all other files
git add .
git commit -m "Initial commit - Task Manager application"
```

### Step 3: Create GitHub Repository
1. Go to https://github.com/
2. Click "+" → "New repository"
3. Name: `task-manager`
4. Description: "Full-stack task management application with Flask"
5. **Don't** initialize with README (you already have one)
6. Click "Create repository"

### Step 4: Push to GitHub
```bash
# Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/task-manager.git

# Push your code
git branch -M main
git push -u origin main
```

**Done!** ✅

## ⚠️ Security Checklist

Before pushing, verify:

1. **Check .gitignore is working:**
   ```bash
   git status
   ```
   
   **Should NOT see:**
   - `venv/`
   - `instance/`
   - `__pycache__/`
   - `.pyc` files

2. **If you see them:**
   ```bash
   # Remove from git tracking
   git rm -r --cached venv/
   git rm -r --cached instance/
   git rm -r --cached __pycache__/
   
   # Commit the removal
   git commit -m "Remove sensitive files"
   ```

3. **Double-check config.py:**
   - Current secret key is fine (it's just a dev key)
   - When deploying, you'll use environment variables

## 📝 What to Put in GitHub Description

**Repository Description:**
"Full-stack task management web application built with Flask and SQLAlchemy. Features user authentication, CRUD operations, task categorization, priorities, and due dates."

**Topics to add:**
- flask
- python
- sqlalchemy
- web-development
- full-stack
- task-manager
- authentication

## 🔗 After Publishing

Update your portfolio website:
1. Get your GitHub URL: `https://github.com/YOUR_USERNAME/task-manager`
2. Add it to your portfolio project links
3. Update and upload your portfolio `index.html`

## 🎯 Repository README

Your README.md is already set up with:
- ✅ Project description
- ✅ Features list
- ✅ Installation instructions
- ✅ Usage guide
- ✅ Tech stack
- ✅ Screenshots section (add yours later)

This makes your repository professional and portfolio-ready!

## 💡 Pro Tips

1. **Keep .gitignore first** - Always commit .gitignore before anything else
2. **Check before pushing** - Always run `git status` to verify what's being uploaded
3. **Write good commit messages** - Clear, descriptive messages
4. **Update regularly** - As you add features, commit and push

## 🚨 If You Accidentally Uploaded Sensitive Files

**If instance/ or venv/ got uploaded:**

1. **Remove from repository:**
   ```bash
   git rm -r --cached instance/
   git rm -r --cached venv/
   git commit -m "Remove sensitive files"
   git push
   ```

2. **Verify .gitignore** is working
3. **Re-push**

**If your database with real user data got uploaded:**
1. Delete the repository on GitHub
2. Create a new one
3. Make sure .gitignore is set up first
4. Upload again

---

**Remember:** When in doubt, check what's being uploaded with `git status` before pushing! 🔒
