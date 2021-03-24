from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/')
def index():
    # testData = test.query.all()

    return render_template('index.html')#, test1 = testData)

@app.route('/my_assessments')
def my_assessments ():
    return render_template('my_assessments.html')

@app.route('/completed_assessments')
def completed_assessments ():
    return render_template('completed_assessments.html')

@app.route('/assessment_statistics')
def assessment_statistics ():
    return render_template('assessment_statistics.html')
