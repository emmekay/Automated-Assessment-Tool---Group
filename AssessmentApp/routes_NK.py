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


@app.route("/completed_assessments/<int:user_id>/<int:module_id>")  # NK
def completed_assessments(user_id, module_id):
    assessments = (
        db.session.query(
            assessment_details, modules_enrolment, assessment_results
        ).filter(
            assessment_results.user_id == current_user.id
            and assessment_results.user_id == modules_enrolment.user_id
            and modules_enrolment.module_id == assessment_details.module_id
        )
    ).all()
    return render_template("completed_assessments.html", Assessments=assessments)


@app.route("/assessment_statistics/<int:assess_id>")  # NK
def assessment_statistics(assess_id):
    module = modules.query.filter(
        modules.module_id == assess_id
    ).first()  # Need to link tables here
    assname = assessment_details.query.filter(
        assessment_details.module_id == assess_id
    ).first()
    attempt = assessment_results.query.filter(
        assessment_results.assessment_id == assess_id
    ).first()
    results = assessment_results.query.filter(
        assessment_results.assessment_id == assess_id
    )
    return render_template(
        "assessment_statistics.html",
        Results=results,
        Module=module,
        Assname=assname,
        Attempt=attempt,
    )


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
