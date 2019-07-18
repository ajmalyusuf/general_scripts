from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms.widgets import PasswordInput

class TaskForm(FlaskForm):
    """
    Form for admin to configure runbook tasks
    """
    name = StringField('Name', validators=[DataRequired()])
    service = StringField('Service', validators=[DataRequired()])
    component = StringField('Component', validators=[DataRequired()])
    description = TextAreaField('Description')
    yaml_name = StringField('YAML Name', validators=[DataRequired()])
    recommendation = TextAreaField('Recommendation', validators=[DataRequired()])
    show_results = BooleanField('Show Results')
    ss_bundle = TextAreaField('SS Test Bundle', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserForm(FlaskForm):
    """
    Form for admin to add/modifiy users
    """
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('New Password', widget=PasswordInput(hide_value=False), validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = StringField('Repeat Password', widget=PasswordInput(hide_value=False))
    email = StringField('Email', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    is_admin = BooleanField('Admin')
    submit = SubmitField('Submit')

class StepForm(FlaskForm):
    """
    Form for admin to add/modifiy steps
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    step_action = StringField('Step Action', validators=[DataRequired()])
    action_string = TextAreaField('Action String')
    secondary_regex = TextAreaField('Secondary Regex')
    filename_mask = StringField('Filename Mask', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ScriptForm(FlaskForm):
    """
    Form for admin to add/modifiy scripts
    """
    name = StringField('Name', validators=[DataRequired()])
    path = StringField('Path and Script name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')


