from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, InputRequired, Regexp
from AssessmentApp.models import *

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max = 40)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max = 40)])
    password = PasswordField('Password',validators=[DataRequired(),Regexp('^.{6,8}$',message='Your password should be between 6 and 8 characters long.')])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password', message='Passwords do not match.')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        User = user.query.filter_by(username=username.data).first()
        if User is not None:
            raise ValidationError('Username already exists. Please choose a different one.')

    def validate_email(self, email):
        User = user.query.filter_by(email=email.data).first()
        if User is not None:
            raise ValidationError('Email is already asocciated with another account, please use another.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

"""
class Survey(FlaskForm):
    question_1 = StringField('On a scale of 1-5, with 1 being very easy and 5 being very difficult, how easy would you rate this assessment?', validators=[
        DataRequired(), Length(min=1, max=1)])
    question_2 = StringField('On a scale of 1-5, with 1 being not at all relevant and 5 relevant to all material, how relevant would you rate this assessment to the teaching you have learned in this module?', validators=[
        DataRequired(), Length(min=1, max=1)])
    question_3 = StringField('On a scale of 1-5, with 1 being very easy and 5 being very difficult, how easy would you rate this assessment?', validators=[
        DataRequired(), Length(min=1, max=1)])
    question_4 = StringField('On a scale of 1-5, with 1 being very easy and 5 being very difficult, how easy would you rate this assessment?', validators=[
        DataRequired(), Length(min=1, max=1)])
    question_5 = StringField('On a scale of 1-5, with 1 being very easy and 5 being very difficult, how easy would you rate this assessment?', validators=[
        DataRequired(), Length(min=1, max=1)])
    question_6 = StringField('On a scale of 1-5, with 1 being very easy and 5 being very difficult, how easy would you rate this assessment?', validators=[
        DataRequired(), Length(min=0, max=2000)])
    submit = SubmitField('Submit')"""

"""class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[InputRequired()])
    submit = SubmitField('Post comment')
"""
