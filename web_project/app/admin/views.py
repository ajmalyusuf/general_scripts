from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required

from . import admin
from forms import TaskForm
from forms import UserForm
from forms import StepForm
from forms import ScriptForm
from .. import db
from ..models import Task
from ..models import User
from ..models import Step
from ..models import Script

password_initializer = '**********'

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

def add_edit_form_template(action, entity, form):
    """
    Same form is used for most of the add/edit screens
    """
    return render_template('common/add_edit_form.html',
                        action=action, entity=entity, form=form)

#########  USER SECTION ##########

@admin.route('/users', methods=['GET', 'POST'])
@login_required
def list_users():
    check_admin()
    users = User.query.all()
    return render_template('admin/users/users.html',
                           entity="User", users=users, title="Users")

@admin.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    check_admin()
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    is_admin=form.is_admin.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You have successfully added a new user.')
        except:
            flash('Error: username already exists.')
        return redirect(url_for('admin.list_users'))

    return add_edit_form_template("Add", "User", form)

@admin.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    check_admin()
    user = User.query.get_or_404(id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.username=form.username.data
        user.email=form.email.data
        if form.password.data != password_initializer:
            user.password=form.password.data
        user.first_name=form.first_name.data
        user.last_name=form.last_name.data
        user.is_admin=form.is_admin.data

        db.session.commit()
        flash('You have successfully edited the user.')
        return redirect(url_for('admin.list_users'))

    form.password.data = password_initializer
    form.confirm.data = password_initializer
    return add_edit_form_template("Edit", "User", form)

@admin.route('/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    check_admin()

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('You have successfully deleted the user.')

    # redirect to the users page
    return redirect(url_for('admin.list_users'))

    return render_template(title="Delete user")


#########  TASK SECTION ##########
@admin.route('/tasks', methods=['GET', 'POST'])
@login_required
def list_tasks():
    """
    List all tasks
    """
    check_admin()
    tasks = Task.query.all()
    return render_template('admin/tasks/tasks.html',
                           entity="Task", tasks=tasks, title="Tasks")

@admin.route('/tasks/add', methods=['GET', 'POST'])
@login_required
def add_task():
    check_admin()

    form = TaskForm()
    if form.validate_on_submit():
        task = Task(name=form.name.data,
                    service=form.service.data,
                    component=form.component.data,
                    description=form.description.data,
                    yaml_name=form.yaml_name.data,
                    ss_bundle=form.ss_bundle.data,
                    recommendation=form.recommendation.data,
                    show_results=form.show_results.data)
        try:
            db.session.add(task)
            db.session.commit()
            flash('You have successfully added a new task.')
        except:
            flash('Error: task name already exists.')
        return redirect(url_for('admin.list_tasks'))
    return add_edit_form_template("Add", "Task", form)

@admin.route('/tasks/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    check_admin()
    add_task = False
    task = Task.query.get_or_404(id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.name=form.name.data
        task.service=form.service.data
        task.component=form.component.data
        task.description=form.description.data
        task.yaml_name=form.yaml_name.data
        task.ss_bundle=form.ss_bundle.data
        task.recommendation=form.recommendation.data
        task.show_results=form.show_results.data
        
        db.session.commit()
        flash('You have successfully edited the task.')
        return redirect(url_for('admin.list_tasks'))

    return add_edit_form_template("Edit", "Task", form)

@admin.route('/tasks/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_task(id):
    check_admin()

    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash('You have successfully deleted the task.')

    return redirect(url_for('admin.list_tasks'))

    return render_template(title="Delete task")


#########  STEP SECTION ##########

@admin.route('/steps/task_id:<int:task_id>', methods=['GET', 'POST'])
@login_required
def list_steps(task_id):
    check_admin()

    task = Task.query.get_or_404(task_id)
    steps = Step.query.filter(Step.task_id == task_id).all()

    return render_template('admin/tasks/steps.html',
                           entity="Step", steps=steps, title="Steps", task=task)

@admin.route('/steps/add/task_id:<int:task_id>', methods=['GET', 'POST'])
@login_required
def add_step(task_id):
    check_admin()
    add_step = True

    form = StepForm()
    if form.validate_on_submit():
        step = Step(name=form.name.data,
                    description=form.description.data,
                    step_action=form.step_action.data,
                    action_string=form.action_string.data,
                    secondary_regex=form.secondary_regex.data,
                    filename_mask=form.filename_mask.data,
                    task_id=task_id)
        try:
            db.session.add(step)
            db.session.commit()
            flash('You have successfully added a new step.')
        except:
            flash('Error: name already exists.')

        return redirect(url_for('admin.list_steps', task_id=task_id))
    return add_edit_form_template("Add", "Step", form)

@admin.route('/steps/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_step(id):
    check_admin()
    add_step = False
    step = Step.query.get_or_404(id)
    form = StepForm(obj=step)
    if form.validate_on_submit():
        step.name=form.name.data
        step.description=form.description.data
        step.step_action=form.step_action.data
        step.action_string=form.action_string.data
        step.secondary_regex=form.secondary_regex.data
        step.filename_mask=form.filename_mask.data

        db.session.commit()
        flash('You have successfully edited a step.')

        return redirect(url_for('admin.list_steps', task_id=step.task_id))

    return add_edit_form_template("Edit", "Step", form)

@admin.route('/steps/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_step(id):
    """
    Delete a step from the database
    """
    check_admin()

    step = Step.query.get_or_404(id)
    task_id = step.task_id
    db.session.delete(step)
    db.session.commit()
    flash('You have successfully deleted the step.')

    return redirect(url_for('admin.list_steps', task_id=task_id))

    return render_template(title="Delete user")

#########  SCRIPT SECTION ##########

@admin.route('/scripts', methods=['GET', 'POST'])
@login_required
def list_scripts():
    """
    List all scripts
    """
    check_admin()

    scripts = Script.query.all()
    print scripts

    return render_template('admin/scripts/scripts.html',
                           entity="Script", scripts=scripts, title="Scripts")

@admin.route('/scripts/add', methods=['GET', 'POST'])
@login_required
def add_script():
    check_admin()
    form = ScriptForm()
    if form.validate_on_submit():
        script = Script(name=form.name.data,
                    path=form.path.data,
                    description=form.description.data)
        try:
            db.session.add(script)
            db.session.commit()
            flash('You have successfully added a new script.')
        except:
            flash('Error: name already exists.')

        return redirect(url_for('admin.list_scripts'))
    return add_edit_form_template("Add", "Script", form)

@admin.route('/scripts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_script(id):
    check_admin()
    script = Script.query.get_or_404(id)
    form = ScriptForm(obj=script)
    if form.validate_on_submit():
        script.name=form.name.data
        script.path=form.path.data
        script.description=form.description.data

        db.session.commit()
        flash('You have successfully edited the script.')
        return redirect(url_for('admin.list_scripts'))

    return add_edit_form_template("Edit", "Script", form)

@admin.route('/scripts/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_script(id):
    check_admin()

    script = Script.query.get_or_404(id)
    db.session.delete(script)
    db.session.commit()
    flash('You have successfully deleted the script.')

    # redirect to the scripts page
    return redirect(url_for('admin.list_scripts'))

    return render_template(title="Delete script")

