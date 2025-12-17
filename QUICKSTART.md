# Quick Start Guide - Task Manager

## 🚀 Get Running in 5 Minutes!

### Step 1: Open Terminal in Project Folder

```bash
# Navigate to the task-manager folder
cd C:\Users\js_cust_PC2025\Documents\portfolio_projects\task-manager
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

```bash
venv\Scripts\activate
```

You should see `(venv)` in your terminal now!

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Flask and all necessary packages.

### Step 5: Run the App!

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Running on http://localhost:5000
```

### Step 6: Open in Browser

Open your browser and go to:
```
http://localhost:5000
```

## ✅ You're Done!

You should see the Task Manager landing page!

## 🎯 Next Steps

1. **Create an Account**
   - Click "Get Started"
   - Fill in username, email, password
   - Click "Create Account"

2. **Create Your First Task**
   - Log in
   - Click "Tasks" in navigation
   - Click "+ New Task"
   - Fill in details
   - Click "Save Task"

3. **Explore the Dashboard**
   - Click "Dashboard"
   - See your task statistics
   - View recent and upcoming tasks

## 🐛 Troubleshooting

**If you get "python: command not found":**
```bash
# Try python3
python3 -m venv venv
```

**If activation doesn't work:**
```bash
# Make sure you're in the project folder
cd C:\Users\js_cust_PC2025\Documents\portfolio_projects\task-manager

# Then activate
venv\Scripts\activate
```

**If port 5000 is already in use:**
```bash
# Edit app.py, change the last line to:
if __name__ == '__main__':
    app.run(debug=True, port=5001)

# Then run again
python app.py
```

**If you see "ModuleNotFoundError":**
```bash
# Make sure virtual environment is activated (you see (venv))
# Then reinstall
pip install -r requirements.txt
```

## 📝 Important Commands

**Start the app:**
```bash
# Make sure venv is activated first!
python app.py
```

**Stop the app:**
```
Press Ctrl+C in the terminal
```

**Deactivate virtual environment:**
```bash
deactivate
```

**Reactivate later:**
```bash
# Navigate to project folder
cd C:\Users\js_cust_PC2025\Documents\portfolio_projects\task-manager

# Activate
venv\Scripts\activate

# Run
python app.py
```

## 🎨 Customizing

Want to change colors or styling?
- Edit `static/css/style.css`
- Look for `:root` section at the top
- Change color values
- Refresh browser to see changes

## 📸 Screenshots for Portfolio

Once it's running, take screenshots of:
1. Landing page
2. Dashboard with tasks
3. Task creation modal
4. Task list with filters

Use these in your portfolio!

## 🚀 When Ready to Deploy

Check the README.md for:
- Railway deployment steps
- Render deployment steps
- Environment variable setup

---

**Need help? Check the full README.md or ask for assistance!** 💪
