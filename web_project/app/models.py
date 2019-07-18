from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User:- Id:{}, Username:{}>'.format(self.id,self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Class to handle Runbook Task
class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(60), index=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(200))
    component = db.Column(db.String(60))
    yaml_name = db.Column(db.String(150))
    ss_bundle = db.Column(db.String(1000))
    recommendation = db.Column(db.String(32000))
    show_results = db.Column(db.Boolean, default=True)
    steps = db.relationship('Step', backref='task',
                                lazy='dynamic')
    conditions = db.relationship('Condition', backref='step',
                                lazy='dynamic')

    def __repr__(self):
        return 'Task:- Id:{}, Name:{}'.format(self.name, self.name)

# Class to handle Task Step
class Step(db.Model):
    __tablename__ = 'steps'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(100))
    step_action = db.Column(db.String(60))
    action_string = db.Column(db.String(500))
    secondary_regex = db.Column(db.String(300))
    filename_mask = db.Column(db.String(500))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    
    def __repr__(self):
        return 'Step:- Id:{}, Name:{}'.format(self.id, self.name)

# Class to handle Step Condition
class Condition(db.Model):
    __tablename__ = 'conditions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    is_logical = db.Column(db.Boolean, default=True)
    jinja_template = db.Column(db.String(1000))
    match_criterion = db.Column(db.String(60))
    match_value = db.Column(db.String(60))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    
    def __repr__(self):
        return 'Condition:- Id:{}, Name:{}'.format(self.id, self.name)

# Class to handle Script
class Script(db.Model):
    __tablename__ = 'scripts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    path = db.Column(db.String(100))
    description = db.Column(db.String(100))
    
    def __repr__(self):
        return 'Script:- Id:{}, Name:{}'.format(self.id, self.name)

# Class to handle Script Args
class ScriptArg(db.Model):
    __tablename__ = 'scripts_args'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    type = db.Column(db.String(60))
    script_id = db.Column(db.Integer, db.ForeignKey('scripts.id'))
    
    def __repr__(self):
        return 'ScriptArg:- Id:{}, Name:{}'.format(self.id, self.name)
