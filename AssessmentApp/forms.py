from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, InputRequired, Regexp
from AssessmentApp.models import user

"""class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstname = StringField('First Name', validators=[DataRequired(), Length(max = 40)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max = 40)])
    password = PasswordField('Password',validators=[DataRequired(),Regexp('^.{6,8}$',message='Your password should be between 6 and 8 characters long.')])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password', message='Passwords do not match.')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email is already asocciated with another account, please use another.')"""

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

"""class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[InputRequired()])
    submit = SubmitField('Post comment')
"""
