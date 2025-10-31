# Task Management API

A RESTful API built with FastAPI for managing tasks with user authentication.

## Features
- User registration and JWT authentication
- Create, read, update, delete tasks
- Filter tasks by completion status and category
- Due date tracking
- SQLite database

## Tech Stack
- FastAPI
- SQLAlchemy
- JWT Authentication
- SQLite

## Installation

1. Clone the repository:
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/task-management-api.git
cd task-management-api
\`\`\`

2. Create virtual environment:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Run the server:
\`\`\`bash
python main.py
\`\`\`

5. Open API docs: http://localhost:8000/docs

## API Endpoints

### Authentication
- `POST /register` - Register new user
- `POST /token` - Login and get access token

### Tasks
- `GET /tasks` - Get all tasks (with optional filters)
- `POST /tasks` - Create new task
- `GET /tasks/{id}` - Get specific task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

## Example Usage

### Register
\`\`\`bash
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","username":"user","password":"pass123"}'
\`\`\`

### Create Task
\`\`\`bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"My Task","description":"Do something"}'
\`\`\`

## Future Enhancements
- [ ] Task priorities
- [ ] Task tags
- [ ] Task sharing
- [ ] Search functionality
- [ ] PostgreSQL support
- [ ] Docker deployment

## License
MIT