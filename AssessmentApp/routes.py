from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/')
def index():
    # testData = test.query.all()
    user1 = user.query.filter_by(id=1).first()

    print("Bool test")
    print(user1.is_staff)

    return render_template('index.html')#, test1 = testData)


@app.route('/addAss')
def addAss():

    return render_template('AssessmentDetails.html')

@app.route('/assessment/<int:id>')
def Ass(id):

    ass = assessment_details.query.filter_by(id=id).first()


    questionIds = assessment_questions.query.filter_by(assessment_id=id).all()

    assQuestions = [ question.query.filter_by(id=q.id).first() for q in questionIds]

    return render_template('UndertakeAss.html',  assQuestions =assQuestions, ass = ass)
