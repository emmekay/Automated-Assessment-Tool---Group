from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Regexp
from AssessmentApp.models import user

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')