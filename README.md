# Task Manager Application

A full-stack web application for task management built with Flask, SQLAlchemy, and modern web technologies.

## 📋 Features

✅ **User Authentication**
- Secure registration and login
- Password hashing with Werkzeug
- Session management with Flask-Login

✅ **Task Management**
- Create, read, update, and delete tasks
- Organize tasks with categories
- Set priority levels (low, medium, high)
- Track status (pending, in progress, completed)
- Set due dates for deadlines

✅ **Dashboard & Analytics**
- View task statistics
- Recent tasks overview
- Upcoming deadlines
- Progress tracking

✅ **Modern UI**
- Responsive design
- Clean, intuitive interface
- Real-time updates
- Filter and search capabilities

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
   ```bash
   cd task-manager
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
task-manager/
├── app.py                  # Main Flask application
├── models.py               # Database models (User, Task)
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Stylesheets
│   └── js/
│       └── main.js        # Client-side JavaScript
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Landing page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── dashboard.html     # Dashboard
│   └── tasks.html         # Task management
└── instance/
    └── tasks.db           # SQLite database (auto-created)
```

## 🔧 Tech Stack

**Backend:**
- Flask (Web framework)
- Flask-SQLAlchemy (ORM)
- Flask-Login (Authentication)
- SQLite (Database - development)
- Werkzeug (Password hashing)

**Frontend:**
- HTML5
- CSS3 (Custom styling)
- JavaScript (Vanilla)

## 💻 Usage

### Creating an Account

1. Navigate to http://localhost:5000
2. Click "Get Started" or "Register"
3. Fill in your details:
   - Username
   - Email
   - Password
4. Click "Create Account"

### Managing Tasks

**Create a Task:**
1. Log in to your account
2. Go to "Tasks" page
3. Click "+ New Task"
4. Fill in task details:
   - Title (required)
   - Description
   - Category
   - Priority
   - Status
   - Due Date
5. Click "Save Task"

**Edit a Task:**
1. Find your task
2. Click the edit icon (✏️)
3. Update the details
4. Save changes

**Delete a Task:**
1. Find your task
2. Click the delete icon (🗑️)
3. Confirm deletion

**Filter Tasks:**
- Use the filter dropdowns to view:
  - By status (Pending, In Progress, Completed)
  - By priority (Low, Medium, High)
  - By category

## 🎯 API Endpoints

### Authentication
- `GET /` - Landing page
- `GET /register` - Registration page
- `POST /register` - Create new user
- `GET /login` - Login page
- `POST /login` - Authenticate user
- `GET /logout` - Logout

### Dashboard
- `GET /dashboard` - User dashboard with statistics

### Tasks
- `GET /tasks` - Task management page
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task

## 🔐 Security Features

- Password hashing with Werkzeug
- CSRF protection with Flask-WTF
- Session-based authentication
- SQL injection protection (SQLAlchemy ORM)
- Input validation

## 🚀 Deployment

### Railway Deployment

1. Create a Railway account at https://railway.app
2. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```
3. Login to Railway:
   ```bash
   railway login
   ```
4. Initialize project:
   ```bash
   railway init
   ```
5. Add PostgreSQL database:
   ```bash
   railway add postgresql
   ```
6. Deploy:
   ```bash
   railway up
   ```

### Render Deployment

1. Create account at https://render.com
2. Create new Web Service
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`
6. Add environment variable:
   - `PYTHON_VERSION`: `3.11.0`
7. Deploy!

## 🧪 Testing

**Test User Registration:**
```bash
# Start the app
python app.py

# In browser:
1. Go to http://localhost:5000
2. Register new account
3. Verify you can log in
```

**Test Task Creation:**
```bash
1. Log in
2. Navigate to Tasks
3. Create a new task
4. Verify it appears in the list
5. Try editing and deleting
```

## 📝 Development

**Adding New Features:**

1. **Backend** (app.py):
   - Add new routes
   - Add view functions
   - Update database models if needed

2. **Frontend** (templates/):
   - Create/update HTML templates
   - Add styles in static/css/style.css
   - Add JavaScript in static/js/main.js

3. **Database** (models.py):
   - Add new models or fields
   - Run migrations if using Flask-Migrate

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Kill process on port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:5000 | xargs kill -9
```

**Database errors:**
```bash
# Delete database and recreate
rm instance/tasks.db
python app.py  # Will recreate database
```

**Module not found:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)

## 🎯 Project for Resume

**Description for Resume:**
"Full-stack task management web application built with Flask and SQLAlchemy. Features include user authentication, CRUD operations, real-time dashboard, and responsive UI. Implemented RESTful API endpoints and secure password hashing. Deployed on Railway/Render."

**Key Accomplishments:**
- ✅ Implemented secure user authentication with Flask-Login
- ✅ Designed and built RESTful API with full CRUD functionality
- ✅ Created responsive UI with vanilla JavaScript
- ✅ Utilized SQLAlchemy ORM for database operations
- ✅ Deployed full-stack application to production

## 📄 License

This project is open source and available for use in your portfolio.

## 👤 Author

Justin Sippel
- Portfolio: [Your Portfolio URL]
- GitHub: [Your GitHub URL]
- LinkedIn: [Your LinkedIn URL]

---

**Built as Project 2 in the Portfolio Project Series** 🚀
