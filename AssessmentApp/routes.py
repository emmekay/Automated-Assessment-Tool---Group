from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/')
def index():
    # testData = test.query.all()

    return render_template('index.html')#, test1 = testData)


@app.route('/addAss')
def addAss():
    # testData = test.query.all()

    return render_template('AssessmentDetails.html')#, test1 = testData)
