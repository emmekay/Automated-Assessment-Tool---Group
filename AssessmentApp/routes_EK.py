from re import S
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy, functools
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from flask_wtf import FlaskForm
from sqlalchemy import func
from sqlalchemy.sql.functions import count

# from datetime import datetime


# from datetime import datetime


from AssessmentApp import *
from AssessmentApp import app, db
from AssessmentApp.models import *
from AssessmentApp.forms import *


@app.route("/survey/<int:mod_id>/<int:asse_id>", methods=["GET", "POST"])
def survey(mod_id, asse_id):

    if request.method == "POST":
        question_1 = request.form["question_1"]
        question_2 = request.form["question_2"]
        question_3 = request.form["question_3"]
        question_4 = request.form["question_4"]
        question_5 = request.form["question_5"]
        question_6 = request.form["question_6"]
        survey1 = surveyinput(
            user_id=current_user.id,
            module_id=mod_id,
            assessment_id=asse_id,
            question_1=question_1,
            question_2=question_2,
            question_3=question_3,
            question_4=question_4,
            question_5=question_5,
            question_6=question_6,
        )

        db.session.add(survey1)
        db.session.commit()
        # flash('Survey Submitted')
        return redirect(url_for("surveysubmit"))
    # surveys = Survey.query.filter(Survey)
    # return str(mod_id) + str(asse_id)
    return render_template(
        "survey.html", title="Survey", mod_id=mod_id, asse_id=asse_id
    )  # , form=form)


@app.route("/myaccount")  # EK
def myaccount():
    Modules = modules.query.all()
    return render_template("myaccount.html", title="My Account", Modules=Modules)


@app.route("/surveysubmit")  # EK
def surveysubmit():
    return render_template("surveysubmit.html", title="Submission Successful")


@app.route("/surveyresults")
def surveyresults():

    Modules = modules_enrolment.query.filter_by(user_id = current_user.id).all()
    enrolled_mod = []
    for m in Modules:
        enrolled_mod.append(m.module_id)

    Assessments = {}

    Assessments_id = []


    for m_id in enrolled_mod:

        temp = []

        Asse = assessment_details.query.filter_by(module_id = m_id).all()

        for a in Asse:
            temp.append(a.id)
            Assessments_id.append(a.id)

        Assessments[m_id] = temp


    # print(Assessments_id)

    survey_Results = {}

    for a_id in Assessments_id:
        temp_answers = [[0,0,0,0,0],[0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        temp_survey = surveyinput.query.filter_by(assessment_id=a_id).all()
        
        for s in temp_survey:
            temp_answers[0][s.question_1 - 1] += 1
            temp_answers[1][s.question_2 - 1] += 1
            temp_answers[2][s.question_3 - 1] += 1
            temp_answers[3][s.question_4 - 1] += 1
            temp_answers[4][s.question_5 - 1] += 1
            #ttt = map(sum(temp_answers[0][s.question_1]))
        survey_Results[a_id] =  temp_answers
        #userCount = surveyinput.query.filter_by(assessment_id=a_id).count()
        #ttt = survey_Results[a_id][0]
        #userTot = userCount[a_id]

    #survey_Count = {}

    #for a_id in Assessments_id:
     #   temp_answers = [[0,0,0,0,0],[0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
      #  temp_survey = surveyinput.query.filter_by(assessment_id=a_id).all()
        
       # for s in temp_survey:
        #    temp_answers[0][s.question_1 - 1] += 1
         #   temp_answers[1][s.question_2 - 1] += 1
          #  temp_answers[2][s.question_3 - 1] += 1
           # temp_answers[3][s.question_4 - 1] += 1
            #temp_answers[4][s.question_5 - 1] += 1
        #survey_Results[a_id] =  temp_answers
        #userCount = surveyinput.query.filter_by(assessment_id=a_id).count()
    #for q in temp_:
     #       len(temp_answers[0][s.question_1 -1]) += 1
            #
      #  survey_Count[a_id] = temp_answers.count[0][0]
       # userCount[a_id] = len(temp_answers([[0, 0], [0, 0]]))

        #survey_Count = surveyinput.query.filter(surveyinput.assessment_id ==a_id, temp_answers).count()
    #print(survey_Results)
    #assess 2 = 12 


   

    return render_template(
        "surveyresults.html", title="Feedback Summary", Assessments_id = Assessments_id, survey_Results = survey_Results, enrolled_mod = enrolled_mod, Assessments = Assessments)


 # Pull all survey results
    # survey_res = surveyresults.query.filter_by(assess_id=assessment_id).all()

    # assess_details = assessment_details.query.filter_by(id=assessment_id).first()

    # module_details = modules.query.filter_by(id=assess_details.module_id).first()

    # Caluclate percentages
    
    #all_surveys = []
    #for result in surveyresults:
    #    all_surveys.append(result.survey)
    #    Q1percent = (count(*) * 100.0 ) / ( count(*))"""
    # Total Question Counts
    # Total Questions by Mod 1 Assess 1
    #'''m1a1qtot = surveyinput.query.filter(
    #    surveyinput.module_id == 1,
    #    surveyinput.assessment_id == 1,
    #    surveyinput.question_1,
    #).count()
    ## Total Questions by Mod 1 Assess 2
    #m1a2qtot = surveyinput.query.filter(
    #    surveyinput.module_id == 1,
    #    surveyinput.assessment_id == 2,
    #    surveyinput.question_1,
    #).count()
    # Total Questions Mod 2 Assess 1
    #m2a1qtot = surveyinput.query.filter(surveyinput.module_id == 2,surveyinput.assessment_id == 1,surveyinput.question_1,).count()
    # Total Questions Mod 2 Assess 2
    #m2a2qtot = surveyinput.query.filter(
    #    surveyinput.module_id == 2,
    #    surveyinput.assessment_id == 2,
    #    surveyinput.question_1,
    #).count()   # Total Questions Mod 2 Assess 3
    #m2a3qtot = surveyinput.query.filter(
    #    surveyinput.module_id == 2,
    #    surveyinput.assessment_id == 3,
    #    surveyinput.question_1,
    #).count()
    # Total QUestions Mod 2 Assess 4
    #m2a4qtot = surveyinput.query.filter(
    #    surveyinput.module_id == 2,
    #    surveyinput.assessment_id == 4,
    #    surveyinput.question_1,
    #).count()

    # Answer Counts
    # Module 1 Assess 1 Q1
    #m1a1q1_1 = surveyinput.query.filter(
    #    surveyinput.module_id == 1,
    #    surveyinput.assessment_id == 1,
    #    surveyinput.question_1 == 1,
    #).count()
    #m1a1q11per = round((m1a1q1_1 / m1a1qtot) * 100)
    #m1a1q1_2 = surveyinput.query.filter(
    #    surveyinput.module_id == 1,
    #    surveyinput.assessment_id == 1,
    #    surveyinput.question_1 == 2,
    #).count()
    #m1a1q12per = round((m1a1q1_2 / m1a1qtot) * 100)
    #m1a1q1_3 = surveyinput.query.filter(
    #    surveyinput.module_id == 1,
    #    surveyinput.assessment_id == 1,
    #    surveyinput.question_1 == 3,
    #).count()
    #m1a1q13per = round((m1a1q1_3 / m1a1qtot) * 100)
    #m1a1q1_4 = surveyinput.query.filter(
    #    surveyinput.module_id == 1,
    #    surveyinput.assessment_id == 1,
    #    surveyinput.question_1 == 4,
    #).count()
    #m1a1q14per = round((m1a1q1_4 / m1a1qtot) * 100)
    #m1a1q1_5 = surveyinput.query.filter(
     
    #m1a1q21per = round((m1a1q2_1 / m1a1qtot) * 100)
    #m1a1q2_2 = surveyinput.query.filter(
    #    surveyinput.module_id == 1,
    #    surveyinput.assessment_id == 1,
    #    surveyinput.question_1 == 2,
    #).count()
   # print(m1a1q15per)
    # print(Assessments_id)
    # print(Assessments[1])'''


    # print(mod_1, m1a1qtot, m2a1qtot, m2a4qtot)
    # print(q1_1)
    # print(q1_total)

    # m1a1q2tot = surveyinput.query.filter(surveyinput.module_id == 1, surveyinput.assessment_id == 1, surveyinput.question_2).count()  # Question 2
    # m1a1q3tot = surveyinput.query.filter(surveyinput.module_id == 1, surveyinput.assessment_id == 1, surveyinput.question_3).count()  # Question 3
    # m1a1q4tot = surveyinput.query.filter(surveyinput.module_id == 1, surveyinput.assessment_id == 1, surveyinput.question_4).count()  # Question 4
    # m1a1q5tot = surveyinput.query.filter(surveyinput.module_id == 1, surveyinput.assessment_id == 1, surveyinput.question_5).count()  # Question 5

    # @app.route("/surveyresults/<int:mod_id>/<int:assess_id>/<question_1>")
    # , surveyinput.question_1, surveyinput.module_id).group_by(
    # surveyinput.question_1, surveyinput.module_id).all()
    # print(result)
    # def surveyresults(mod_id, assess_id, question_1):
    # q1results = surveyinput.query.group_by(mod_id=mod_id, assess_id=assess_id, question_1=question_1).all()
    # print(q1results)
    # atr = surveyinput.query.filter_by(user_id=current_user.id, assessment_id=id).all()
    # question_1 = surveyinput.query.filter_by(question_1=question_1).all()
    # ass = surveyinput.query.filter_by(question_1 = question_1).first()
    # @app.route("/surveyresults/<int:mod_id>/<int:assess_id>/<int:survey_id>")  # EK
    # @app.route("/surveyresults/<int:>/<int:asse_id>", methods=['GET'])

    # question_1 = surveyinput.question_1
    # surv = surveyinput.query.filter_by(id=id).first()
    # questionIds = assessment_questions.query.filter_by(assessment_id=id).all()

    # q1response = [question_1.query.filter_by(id=q.question_id).first() for q in surv]
    # current_user.id
    # print(q1response)
    # select 'question_1', cast(count(*) * 100.0 / (select count(*)) from surveyinput)
    # WHERE `question_1` = 3
    # group by 'question_1'
    # SELECT module_id, assessment_id, question_1, count(*) cnt FROM surveyinput group by module_id, assessment_id, question_1

    # questionIds = assessment_questions.query.filter_by(assessment_id=id).all()

    # all_surveys = []
    # for result in q1results:
    #   all_surveys.append(result.question_1)
    # q1_choice1 = (all_surveys.count(str(1)))
    # return render_template('surveyresults.html', title='Feedback Summary')
    # return render_template('surveyresults.html', q1_choice1 = q1_choice1, title='Feedback Summary')

    # Pull all survey results
    # survey_res = surveyresults.query.filter_by(assess_id=assessment_id).all()

    # @app.route("/survey")
    # def survey():
    # print("Total number of surveys is", survey.query.count())
    #   return render_template('survey.html', title='Assessment Completed')
