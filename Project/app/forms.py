from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, DateField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AddEventForm(FlaskForm):
   name = StringField('Name', validators=[DataRequired()])
   date = DateField('Date', validators=[DataRequired()])
   organizer = StringField('Organizer', validators=[DataRequired()])
   location = StringField('Location', validators=[DataRequired()])
   description = TextAreaField('Description', validators=[DataRequired()])