from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from statistics import mean

from AssessmentApp import app, db
from AssessmentApp.models import *


@app.route("/my_assessments")  # NK
def my_assessments():
    return render_template("my_assessments.html")


@app.route("/completed_assessments/<int:module_id>")  # NK
def completed_assessments(module_id):
    # print(current_user.id)
    res = assessment_results.query.filter_by(user_id=current_user.id).all()
    # print(res[0].grade)

    asse_id = []
    asse_details = {}

    for r in res:
        if r.assessment_id not in asse_id:
            asse_id.append(r.assessment_id)

    for a_id in asse_id:
        temp = assessment_details.query.filter_by(id=a_id).first()
        asse_details[a_id] = temp

    # print(asse_details[res[0].assessment_id].assessment_name)



    # for(r in res):
    #     print(r.grade)


    # print(res[0].grade)
    # assessments = (
    #     db.session.query(
    #         assessment_details, modules_enrolment, assessment_results
    #     ).filter(
    #         assessment_results.user_id == current_user.id
    #         and assessment_results.user_id == modules_enrolment.user_id
    #         and modules_enrolment.module_id == assessment_details.module_id
    #     )
    # ).all()
    return render_template("completed_assessments.html", res = res, asse_details = asse_details)


@app.route("/assessment_statistics/<int:assess_id>")  # NK
def assessment_statistics(assess_id):

    # All of students results for this assesment
    res = assessment_results.query.filter_by(user_id=current_user.id, assessment_id =assess_id).all()

    # All of class results for this assesmnt
    res_all = assessment_results.query.filter_by(assessment_id =assess_id).all()

    # calc avg
    temp = []
    for r in res_all:
        temp.append(r.grade)


    avg1 = sum(temp) / len(temp)

    # Assesment details
    asse = assessment_details.query.filter_by(id=assess_id).first()


    # module = modules.query.filter(
    #     modules.module_id == assess_id
    # ).first()  # Need to link tables here
    # assname = assessment_details.query.filter(
    #     assessment_details.module_id == assess_id
    # ).first()
    # attempt = assessment_results.query.filter(
    #     assessment_results.assessment_id == assess_id
    # ).first()
    # results = assessment_results.query.filter(
    #     assessment_results.assessment_id == assess_id
    # )
    # return render_template(
    #     "assessment_statistics.html",
    #     Results=results,
    #     Module=module,
    #     Assname=assname,
    #     Attempt=attempt,
    # )
    return render_template(
        "assessment_statistics.html",
        asse= asse,
        avg1 = avg1,
        res = res
    )
    # return str(avg)


def Average(results):
    all_grades = assessment_results.query.filter(
        assessment_results.assessment_id == assess_id
    ).all()
    average = statistics.mean(all_grades)
    return render_template(average=average)


"""
def Average(results):
    all_grades = []
    for ass in results:
        all_grades.appened(ass.grade)
    avg = sum(all_grades) / len(all_grades)
    return avg

def Lowest(grades):
    grade_list=[]
    grade_list.append(grades)
    low = min(grade_list)
    return low

def Highest(grades):
    grade_list=[]
    grade_list.append(grades)
    high=max(grade_list)
    return high

@app.route("/assessment_statistics")
def assessment_stats():
  #enrolled = modules_enrolment.query.all()
  Results = assessment_results.query.all()
  return render_template('assessment_statistics.html', Results=Results)
"""
