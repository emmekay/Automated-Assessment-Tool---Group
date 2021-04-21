from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

from AssessmentApp import app
from AssessmentApp.models import *


@app.route("/survey")
def survey():
    #print("Total number of surveys is", survey.query.count())
    return render_template('survey.html', title='Assessment Completed')


@app.route("/staffaccount")  # EK
def staffaccount():
    return render_template('staffaccount.html', title='My Account')


@app.route("/studentaccount")  # EK
def studentaccount():
    return render_template('studentaccount.html', title='My Account')


@app.route("/surveyresults")  # EK
def surveyresults():
    return render_template('surveyresults.html', title='Feedback Summary')

