from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
#from datetime import datetime 

from AssessmentApp import app, db
from AssessmentApp.models import surveyinput
from AssessmentApp.forms import *


#@app.route("/survey")
#def survey():
    #print("Total number of surveys is", survey.query.count())
 #   return render_template('survey.html', title='Assessment Completed')


@app.route("/survey", methods=['GET', 'POST'])
def survey():
    #form = Survey()
    #if form.validate_on_submit():
    if request.method == "POST":
        question_1 = request.form['question_1']
        question_2 = request.form['question_2']
        question_3 = request.form['question_3']
        question_4 = request.form['question_4']
        question_5 = request.form['question_5']
        question_6 = request.form['question_6']
        
        survey1 = surveyinput(question_1=question_1, question_2=question_2, question_3=question_3,
                         question_4=question_4, question_5=question_5, question_6=question_6)

        """survey1 = survey(question_1=form.question_1.data, question_2=form.question_2.data, question_3=form.question_3.data, question_4=form.question_4.data, question_5=form.question_5.data, question_6=form.question_6.data)"""
        #db.session.add(survey1)
        db.session.add(survey1)
        db.session.commit()
        #flash('Survey Submitted')
        return redirect(url_for('survey'))
    #surveys = Survey.query.filter(Survey)
    return render_template('survey.html', title='Survey')#, form=form)
#user_id=form.user_id.data, assessment_id=form.assessment_id.data,

@app.route("/staffaccount")  # EK
def staffaccount():
    return render_template('staffaccount.html', title='My Account')


@app.route("/studentaccount")  # EK
def studentaccount():
    return render_template('studentaccount.html', title='My Account')


@app.route("/surveyresults")  # EK
def surveyresults():
    return render_template('surveyresults.html', title='Feedback Summary')

