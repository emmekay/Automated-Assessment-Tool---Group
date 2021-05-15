from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, SelectField, BooleanField, DateTimeField, IntegerField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, InputRequired, Regexp, NumberRange

from wtforms.widgets.html5 import DateTimeLocalInput, DateInput
from wtforms.fields.html5 import DateField, TimeField, DateTimeField
# from flask.ext.admin.form import widgets
from AssessmentApp.models import *


class AsseDetails(FlaskForm):

    aType = SelectField('Assessment Type', choices = [(0, 'Summative'), (1, 'Formative')], validators=[DataRequired()])
    aTitle = StringField('Assessment Title', validators=[DataRequired()])
    aTimeAva =  TimeField('Assessment Time Available', validators=[DataRequired()],format='%H:%M')#DateTimeField('Assessment Time Available', validators=[DataRequired()])
    aStart = DateField('Assessment Start Date', validators=[DataRequired()] ,format='%Y-%m-%d')
    aStartTime = TimeField('Assessment Start Date', validators=[DataRequired()],format='%H:%M')
    aEnd = DateField('Assessment End Date', validators=[DataRequired()],format='%Y-%m-%d')#DateTimeField('Assessment End Date', validators=[DataRequired()])
    aEndTime = TimeField('Assessment End Date', validators=[DataRequired()],format='%H:%M')

    aRel = DateField('Assessment Result Date', format='%Y-%m-%d')
    aRelTime = TimeField('Assessment Result Date', format='%H:%M')

    aWeight = DecimalField('Assessment Weighting', validators=[DataRequired(), NumberRange(min=0, max=100, message='Range of (0,100)')])
    aAttemps = IntegerField('Allowed Attempts', validators=[DataRequired(), NumberRange(min=1, max=100, message="Range of (1,100)")])
    aDes = TextAreaField('Assessment Description and Instructions')
    submit = SubmitField('Save')
