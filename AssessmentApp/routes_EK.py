from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from flask_wtf import FlaskForm
#from datetime import datetime




from AssessmentApp import *
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
    #print(mod_id)
    #print(asse_id)
    #print(current_user.id)
    

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
#@app.route("/surveyresults/<int:>/<int:asse_id>", methods=['GET'])
def surveyresults():

    # Pull all survey results 
    #survey_res = surveyresults.query.filter_by(assess_id=assessment_id).all()

    #assess_details = assessment_details.query.filter_by(id=assessment_id).first()

    #module_details = modules.query.filter_by(id=assess_details.module_id).first()

    #Caluclate percentages 
    '''all_surveys = []
    for result in surveyresults:
        all_surveys.append(result.survey)
        Q1percent = (count(*) * 100.0 ) / ( count(*))'''

    
   # rest = surveyinput.query.filter_by(user_id=current_user.id, assessment_id=id).all()
   # res = assessment_results(user_id=current_user.id, assessment_id=id, attempt_number=len(
       # att)+1, grade=round((correct/totalPossibleMarks)*100), date_completed=datetime.now())
    #question = select 'question_1', count(*) * 100.0 / (select count(*) from surveyinput)
    return render_template('surveyresults.html', title='Feedback Summary')


@app.route("/surveysubmit")  # EK
def surveysubmit():
    return render_template('surveysubmit.html', title='Submission Successful')
