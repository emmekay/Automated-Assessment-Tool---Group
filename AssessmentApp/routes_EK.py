from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy, functools
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from flask_wtf import FlaskForm
from sqlalchemy import func

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


# user_id=form.user_id.data, assessment_id=form.assessment_id.data,


@app.route("/myaccount")  # EK
def myaccount():
    Modules = modules.query.all()
    return render_template("myaccount.html", title="My Account", Modules=Modules)


@app.route("/surveysubmit")  # EK
def surveysubmit():
    return render_template("surveysubmit.html", title="Submission Successful")


@app.route("/surveyresults")
def surveyresults():

    # Pull all survey results
    # survey_res = surveyresults.query.filter_by(assess_id=assessment_id).all()

    # assess_details = assessment_details.query.filter_by(id=assessment_id).first()

    # module_details = modules.query.filter_by(id=assess_details.module_id).first()

    # Caluclate percentages
    """all_surveys = []
    for result in surveyresults:
        all_surveys.append(result.survey)
        Q1percent = (count(*) * 100.0 ) / ( count(*))"""
    # Total Question Counts
    # Total Questions by Mod 1 Assess 1
    m1a1qtot = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1,
    ).count()
    # Total Questions by Mod 1 Assess 2
    m1a2qtot = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 2,
        surveyinput.question_1,
    ).count()
    # Total Questions Mod 2 Assess 1
    m2a1qtot = surveyinput.query.filter(
        surveyinput.module_id == 2,
        surveyinput.assessment_id == 1,
        surveyinput.question_1,
    ).count()
    # Total Questions Mod 2 Assess 2
    m2a2qtot = surveyinput.query.filter(
        surveyinput.module_id == 2,
        surveyinput.assessment_id == 2,
        surveyinput.question_1,
    ).count()
    # Total Questions Mod 2 Assess 3
    m2a3qtot = surveyinput.query.filter(
        surveyinput.module_id == 2,
        surveyinput.assessment_id == 3,
        surveyinput.question_1,
    ).count()
    # Total QUestions Mod 2 Assess 4
    m2a4qtot = surveyinput.query.filter(
        surveyinput.module_id == 2,
        surveyinput.assessment_id == 4,
        surveyinput.question_1,
    ).count()

    # Answer Counts
    # Module 1 Assess 1 Q1
    m1a1q1_1 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 1,
    ).count()
    m1a1q11per = round((m1a1q1_1 / m1a1qtot) * 100)
    m1a1q1_2 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 2,
    ).count()
    m1a1q12per = round((m1a1q1_2 / m1a1qtot) * 100)
    m1a1q1_3 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 3,
    ).count()
    m1a1q13per = round((m1a1q1_3 / m1a1qtot) * 100)
    m1a1q1_4 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 4,
    ).count()
    m1a1q14per = round((m1a1q1_4 / m1a1qtot) * 100)
    m1a1q1_5 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 5,
    ).count()
    m1a1q15per = round((m1a1q1_5 / m1a1qtot) * 100)

    # Module 1 Assess 1 Q2
    m1a1q2_1 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 1,
    ).count()
    m1a1q21per = round((m1a1q2_1 / m1a1qtot) * 100)
    m1a1q2_2 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 2,
    ).count()
    m1a1q22per = round((m1a1q2_2 / m1a1qtot) * 100)
    m1a1q2_3 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 3,
    ).count()
    m1a1q23per = round((m1a1q2_3 / m1a1qtot) * 100)

    # Module 1 Assess 1 Q3
    m1a1q3_1 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 1,
    ).count()
    m1a1q31per = round((m1a1q3_1 / m1a1qtot) * 100)
    m1a1q3_2 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 2,
    ).count()
    m1a1q32per = round((m1a1q3_2 / m1a1qtot) * 100)
    m1a1q3_3 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 3,
    ).count()
    m1a1q33per = round((m1a1q3_3 / m1a1qtot) * 100)
    m1a1q3_4 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 4,
    ).count()
    m1a1q34per = round((m1a1q3_4 / m1a1qtot) * 100)
    m1a1q3_5 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 5,
    ).count()
    m1a1q35per = round((m1a1q3_5 / m1a1qtot) * 100)

    # Module 1 Assess 1 Q4
    m1a1q4_1 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 1,
    ).count()
    m1a1q41per = round((m1a1q4_1 / m1a1qtot) * 100)
    m1a1q4_2 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 2,
    ).count()
    m1a1q42per = round((m1a1q4_2 / m1a1qtot) * 100)
    m1a1q4_3 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 3,
    ).count()
    m1a1q43per = round((m1a1q4_3 / m1a1qtot) * 100)
    m1a1q4_4 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 4,
    ).count()
    m1a1q44per = round((m1a1q4_4 / m1a1qtot) * 100)
    m1a1q4_5 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 5,
    ).count()
    m1a1q45per = round((m1a1q4_5 / m1a1qtot) * 100)

    # Module 1 Assess 1 Q5
    m1a1q5_1 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 1,
    ).count()
    m1a1q51per = round((m1a1q5_1 / m1a1qtot) * 100)
    m1a1q5_2 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 2,
    ).count()
    m1a1q52per = round((m1a1q5_2 / m1a1qtot) * 100)
    m1a1q5_3 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 3,
    ).count()
    m1a1q53per = round((m1a1q5_3 / m1a1qtot) * 100)
    m1a1q5_4 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 4,
    ).count()
    m1a1q54per = round((m1a1q5_3 / m1a1qtot) * 100)
    m1a1q5_5 = surveyinput.query.filter(
        surveyinput.module_id == 1,
        surveyinput.assessment_id == 1,
        surveyinput.question_1 == 5,
    ).count()
    m1a1q55per = round((m1a1q5_3 / m1a1qtot) * 100)

    print(m1a1q15per)

    return render_template(
        "surveyresults.html",
        m1a1qtot=m1a1qtot,
        m1a2q2ot=m1a2qtot,
        m2a1qtot=m2a1qtot,
        m2a2qtot=m2a2qtot,
        m2a3qtot=m2a3qtot,
        m2a4qtot=m2a4qtot,
        m1a1q1_1=m1a1q1_1,
        m1a1q1_2=m1a1q1_2,
        m1a1q1_3=m1a1q1_3,
        m1a1q1_4=m1a1q1_4,
        m1a1q1_5=m1a1q1_5,
        m1a1q2_1=m1a1q2_1,
        m1a1q2_2=m1a1q2_2,
        m1a1q2_3=m1a1q2_3,
        m1a1q3_1=m1a1q3_1,
        m1a1q3_2=m1a1q3_2,
        m1a1q3_3=m1a1q3_3,
        m1a1q3_4=m1a1q3_4,
        m1a1q3_5=m1a1q3_5,
        m1a1q4_1=m1a1q4_1,
        m1a1q4_2=m1a1q4_2,
        m1a1q4_3=m1a1q4_3,
        m1a1q4_4=m1a1q4_4,
        m1a1q4_5=m1a1q4_5,
        m1a1q5_1=m1a1q5_1,
        m1a1q5_2=m1a1q5_2,
        m1a1q5_3=m1a1q5_3,
        m1a1q5_4=m1a1q5_4,
        m1a1q5_5=m1a1q5_5,
        m1a1q11per=m1a1q11per,
        m1a1q12per=m1a1q12per,
        m1a1q13per=m1a1q13per,
        m1a1q14per=m1a1q14per,
        m1a1q15per=m1a1q15per,
        m1a1q21per=m1a1q21per,
        m1a1q22per=m1a1q22per,
        m1a1q23per=m1a1q23per,
        m1a1q31per=m1a1q31per,
        m1a1q32per=m1a1q32per,
        m1a1q33per=m1a1q33per,
        m1a1q34per=m1a1q34per,
        m1a1q35per=m1a1q35per,
        m1a1q41per=m1a1q41per,
        m1a1q42per=m1a1q42per,
        m1a1q43per=m1a1q43per,
        m1a1q44per=m1a1q44per,
        m1a1q45per=m1a1q45per,
        m1a1q51per=m1a1q51per,
        m1a1q52per=m1a1q52per,
        m1a1q53per=m1a1q53per,
        m1a1q54per=m1a1q54per,
        m1a1q55per=m1a1q55per,
        title="Feedback Summary",
    )

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
