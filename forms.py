import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, email, EqualTo


class registrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=20, min=2)])
    email = StringField('email', validators=[DataRequired(), email()])
    password = PasswordField('password', validators=[DataRequired()])
    password_validation = PasswordField('password_validation', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('submit')


class loginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('login')
