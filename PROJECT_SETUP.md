# Task Manager - Project Setup Guide

## 📁 Project Structure

```
task-manager/
├── app.py                  # Main Flask application
├── models.py               # Database models
├── config.py               # Configuration
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Styles
│   └── js/
│       └── main.js        # Frontend JavaScript
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Landing page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── dashboard.html     # Main dashboard
│   └── tasks.html         # Task management
└── instance/
    └── tasks.db           # SQLite database (auto-created)
```

## 🔧 Setup Instructions

### 1. Create Project Folder

```bash
# Navigate to your portfolio projects folder
cd C:\Users\js_cust_PC2025\Documents\portfolio_projects

# Create new folder for this project
mkdir task-manager
cd task-manager
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# You should see (venv) in your terminal now
```

### 3. Install Dependencies

```bash
# Install Flask and extensions
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Login
pip install Flask-WTF
pip install email-validator

# Save dependencies
pip freeze > requirements.txt
```

### 4. Create Project Files

Create these files (we'll fill them in next):
- `app.py`
- `models.py`
- `config.py`
- `requirements.txt` (already created)

Create these folders:
- `static/css/`
- `static/js/`
- `templates/`
- `instance/` (will be auto-created)

## 📝 What Each File Does

**app.py** - Main application
- Routes (URLs)
- View functions
- App configuration

**models.py** - Database structure
- User model
- Task model
- Database relationships

**config.py** - Settings
- Secret key
- Database connection
- Environment variables

**templates/** - HTML files
- Jinja2 templates
- Page layouts

**static/** - CSS, JS, images
- Styling
- Frontend logic
- Assets

## 🎯 Development Workflow

1. **Backend first**: Get database and routes working
2. **Test with Postman/browser**: Verify functionality
3. **Frontend**: Build the UI
4. **Integration**: Connect everything
5. **Testing**: Make sure it all works
6. **Deployment**: Push to Railway/Render

## 🧪 Testing Locally

```bash
# Activate virtual environment
venv\Scripts\activate

# Run the app
python app.py

# Open browser to:
http://localhost:5000
```

## 📚 Learning Resources

As we build, you'll learn:
- **Flask routing** - How URLs work
- **SQLAlchemy** - Database operations
- **Jinja2** - Template rendering
- **Forms & validation** - User input
- **Authentication** - Secure login
- **CRUD operations** - Create, Read, Update, Delete

## ⚡ Quick Commands Reference

```bash
# Activate virtual environment
venv\Scripts\activate

# Deactivate virtual environment
deactivate

# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# Run the app
python app.py

# Run in debug mode (auto-reload on changes)
flask run --debug
```

## 🎯 Today's Goal

Get the basic Flask app running with:
- ✅ Database models
- ✅ User registration
- ✅ Basic routing
- ✅ Test it locally

Ready? Let's build it! 🚀
