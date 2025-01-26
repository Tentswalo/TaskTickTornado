from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, mail
from .models import Task, User
from flask_mail import Message
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.order_by(Task.due_date).all()
    return render_template('index.html', tasks=tasks)

@main.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        new_task = Task(title=title, description=description, priority=priority, due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!')
        return redirect(url_for('main.index'))
    return render_template('tasks.html')

@main.route('/send_email/<int:task_id>')
def send_email(task_id):
    task = Task.query.get_or_404(task_id)
    users = User.query.all()
    emails = [user.email for user in users]

    msg = Message(
        subject=f"Reminder: {task.title}",
        sender='your_email@example.com',
        recipients=emails,
        body=f"Task '{task.title}' is due on {task.due_date}."
    )
    mail.send(msg)
    flash('Email notifications sent!')
    return redirect(url_for('main.index'))
