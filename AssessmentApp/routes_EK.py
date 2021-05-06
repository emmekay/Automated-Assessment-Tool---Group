from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from flask_wtf import FlaskForm
#from datetime import datetime





from AssessmentApp import app, db
from AssessmentApp.models import *
from AssessmentApp.forms import *


#@app.route("/survey")
#def survey():
    #print("Total number of surveys is", survey.query.count())
 #   return render_template('survey.html', title='Assessment Completed')


@app.route("/survey/<int:mod_id>/<int:asse_id>", methods=['GET', 'POST'])
def survey(mod_id, asse_id):
    #form = Survey()
    #if form.validate_on_submit():
    print(mod_id)
    print(asse_id)
    print(current_user.id)
    

    if request.method == "POST":
        question_1 = request.form['question_1']
        question_2 = request.form['question_2']
        question_3 = request.form['question_3']
        question_4 = request.form['question_4']
        question_5 = request.form['question_5']
        question_6 = request.form['question_6']
        survey1 = surveyinput(user_id = current_user.id, module_id = mod_id, assessment_id = asse_id, question_1=question_1, question_2=question_2, question_3=question_3,
                         question_4=question_4, question_5=question_5, question_6=question_6)

        db.session.add(survey1)
        db.session.commit()
        #flash('Survey Submitted')
        return redirect(url_for('surveysubmit'))
    #surveys = Survey.query.filter(Survey)
    # return str(mod_id) + str(asse_id)
    return render_template('survey.html', title='Survey', mod_id = mod_id, asse_id = asse_id)#, form=form)
#user_id=form.user_id.data, assessment_id=form.assessment_id.data,

@app.route("/staffaccount")  # EK
def staffaccount():
    Modules = modules.query.all()
    return render_template('staffaccount.html', title='My Account', Modules = Modules )


@app.route("/studentaccount")  # EK
def studentaccount():
    return render_template('studentaccount.html', title='My Account')


@app.route("/surveyresults")  # EK
def surveyresults():
    return render_template('surveyresults.html', title='Feedback Summary')


@app.route("/surveysubmit")  # EK
def surveysubmit():
    return render_template('surveysubmit.html', title='Submission Successful')
