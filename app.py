from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Task
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
with app.app_context():
    db.create_all()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables
with app.app_context():
    db.create_all()


# ============================================================================
# AUTHENTICATION ROUTES
# ============================================================================

@app.route('/')
def index():
    """Landing page"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            flash('All fields are required', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))


# ============================================================================
# DASHBOARD & TASK ROUTES
# ============================================================================

@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard"""
    # Get task statistics
    total_tasks = Task.query.filter_by(user_id=current_user.id).count()
    completed_tasks = Task.query.filter_by(user_id=current_user.id, status='completed').count()
    pending_tasks = Task.query.filter_by(user_id=current_user.id, status='pending').count()
    in_progress_tasks = Task.query.filter_by(user_id=current_user.id, status='in_progress').count()
    
    # Get recent tasks
    recent_tasks = Task.query.filter_by(user_id=current_user.id)\
        .order_by(Task.created_at.desc()).limit(5).all()
    
    # Get upcoming tasks (with due dates)
    upcoming_tasks = Task.query.filter_by(user_id=current_user.id)\
        .filter(Task.due_date.isnot(None), Task.status != 'completed')\
        .order_by(Task.due_date).limit(5).all()
    
    stats = {
        'total': total_tasks,
        'completed': completed_tasks,
        'pending': pending_tasks,
        'in_progress': in_progress_tasks
    }
    
    return render_template('dashboard.html', 
                         stats=stats, 
                         recent_tasks=recent_tasks,
                         upcoming_tasks=upcoming_tasks)


@app.route('/tasks')
@login_required
def tasks():
    """Task management page"""
    # Get filter parameters
    status_filter = request.args.get('status')
    category_filter = request.args.get('category')
    priority_filter = request.args.get('priority')
    show_archived = request.args.get('archived') == 'true'
    
    # Build query
    query = Task.query.filter_by(user_id=current_user.id)
    
    # Filter by archived status
    if show_archived:
        query = query.filter_by(archived=True)
    else:
        query = query.filter_by(archived=False)
    
    if status_filter:
        query = query.filter_by(status=status_filter)
    if category_filter:
        query = query.filter_by(category=category_filter)
    if priority_filter:
        query = query.filter_by(priority=priority_filter)
    
    tasks = query.order_by(Task.created_at.desc()).all()
    
    # Get unique categories for filter dropdown
    categories = db.session.query(Task.category).filter_by(user_id=current_user.id)\
        .distinct().all()
    categories = [c[0] for c in categories if c[0]]
    
    # Count archived tasks
    archived_count = Task.query.filter_by(user_id=current_user.id, archived=True).count()
    
    return render_template('tasks.html', 
                         tasks=tasks, 
                         categories=categories,
                         current_status=status_filter,
                         current_category=category_filter,
                         current_priority=priority_filter,
                         show_archived=show_archived,
                         archived_count=archived_count)


# ============================================================================
# TASK API ENDPOINTS (CRUD Operations)
# ============================================================================

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    """Get a single task"""
    task = Task.query.get_or_404(task_id)
    
    # Check if task belongs to current user
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    return jsonify({'success': True, 'task': task.to_dict()})


@app.route('/api/tasks', methods=['POST'])
@login_required
def create_task():
    """Create a new task"""
    data = request.get_json()
    
    task = Task(
        title=data.get('title'),
        description=data.get('description'),
        category=data.get('category'),
        priority=data.get('priority', 'medium'),
        status=data.get('status', 'pending'),
        notes=data.get('notes'),
        user_id=current_user.id
    )
    
    # Parse due date if provided
    if data.get('due_date'):
        try:
            task.due_date = datetime.fromisoformat(data.get('due_date'))
        except:
            pass
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify({'success': True, 'task': task.to_dict()}), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    """Update a task"""
    task = Task.query.get_or_404(task_id)
    
    # Check if task belongs to current user
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.category = data.get('category', task.category)
    task.priority = data.get('priority', task.priority)
    task.status = data.get('status', task.status)
    task.notes = data.get('notes', task.notes)
    
    # Update due date if provided
    if 'due_date' in data:
        if data['due_date']:
            try:
                task.due_date = datetime.fromisoformat(data['due_date'])
            except:
                pass
        else:
            task.due_date = None
    
    # Mark as completed if status is completed
    if task.status == 'completed' and not task.completed_at:
        task.completed_at = datetime.utcnow()
    elif task.status != 'completed':
        task.completed_at = None
    
    db.session.commit()
    
    return jsonify({'success': True, 'task': task.to_dict()})


@app.route('/api/tasks/<int:task_id>/archive', methods=['PUT'])
@login_required
def archive_task(task_id):
    """Archive or unarchive a task"""
    task = Task.query.get_or_404(task_id)
    
    # Check if task belongs to current user
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    task.archived = data.get('archived', not task.archived)
    
    db.session.commit()
    
    return jsonify({'success': True, 'task': task.to_dict()})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    """Delete a task"""
    task = Task.query.get_or_404(task_id)
    
    # Check if task belongs to current user
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Task deleted'})


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


# ============================================================================
# RUN APP
# ============================================================================

if __name__ == '__main__':
    app.run(debug=True)
