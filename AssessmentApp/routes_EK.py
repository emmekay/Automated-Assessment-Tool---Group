from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


#from datetime import datetime

from AssessmentApp import app, db
from AssessmentApp import models
from AssessmentApp.models import *
from AssessmentApp.forms import *


"""@app.route("/survey")
def survey():
    #print("Total number of surveys is", survey.query.count())
    return render_template('survey.html', title='Assessment Completed')"""


@app.route("/survey", methods=['GET', 'POST'])
def surveyinfo():
    form = Survey()
    if form.validate_on_submit():
        user = Survey(user=models.user_id.data, assessment_id=models.assessment_id.data, question_1=form.question_1.data, question_2=form.question_2.data, question_3=form.question_3.data, question_4=form.question_4.data, question_5=form.question_5.data, question_6=form.question_6.data)
        db.session.add(user)
        db.session.commit()
        flash('Survey Submitted')
        return redirect(url_for('index.html'))
    return render_template('survey.html', title='Survey', form=form)


@app.route("/staffaccount")  # EK
def staffaccount():
    return render_template('staffaccount.html', title='My Account')


@app.route("/studentaccount")  # EK
def studentaccount():
    return render_template('studentaccount.html', title='My Account')


@app.route("/surveyresults")  # EK
def surveyresults():
    return render_template('surveyresults.html', title='Feedback Summary')

