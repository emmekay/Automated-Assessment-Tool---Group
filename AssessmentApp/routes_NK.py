from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/my_assessments') #NK
def my_assessments():
    return render_template('my_assessments.html')


@app.route('/completed_assessments/') #NK
def completed_assessments():
    print(current_user.id)
    return render_template('completed_assessments.html')

@app.route('/assessment_statistics/<int:assess_id>') #NK

def assessment_statistics(assess_id):
    module = modules.query.filter(modules.module_id==assess_id).first()
    assname = assessment_details.query.filter(assessment_details.module_id==assess_id).first()
    attempt = assessment_results.query.filter(assessment_results.assessment_id== assess_id).first()
    results = assessment_results.query.filter(assessment_results.assessment_id==assess_id)
    return render_template('assessment_statistics.html', Results=results, Module=module, Assname=assname, Attempt=attempt)
'''
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
'''
