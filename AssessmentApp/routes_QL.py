from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/createQuestion', methods=['GET', 'POST'])
def createQuestion():
    if request.method == 'POST':
        # Add question type one
        quesTypeOne_Content = request.form['cQ_T1_Question_Content']
        quesTypeOne_DifLevel = request.form['cQ_T1_Difficulty_Level']
        quesTypeOne_Point = request.form['cQ_T1_Point']
        quesTypeOne_Option1 = request.form['cQ_T1_Option1']
        quesTypeOne_Option2 = request.form['cQ_T1_Option2']
        quesTypeOne_Option3 = request.form['cQ_T1_Option3']
        quesTypeOne_Option4 = request.form['cQ_T1_Option4']
        quesTypeOne_CorrAnswer = request.form['cQ_T1_Correct_Answer']
        quesType_one = question(question=quesTypeOne_Content, difficulty=quesTypeOne_DifLevel, value=quesTypeOne_Point,\
                                answer_1=quesTypeOne_Option1, answer_2=quesTypeOne_Option2, answer_3=quesTypeOne_Option3,\
                                answer_4=quesTypeOne_Option4, correct_answer=quesTypeOne_CorrAnswer,)
        db.session.add(quesType_one)
        db.session.commit()
        return redirect(url_for(createQuestion))

        # Add question type two
        quesTypeTwo_Content = request.form['QContent']
        quesTypeTwo_DifLevel = request.form['DifficultyLevel']
        quesTypeTwo_Point = request.form['Points']
        quesTypeTwo_Option1 = request.form['Option1']
        quesTypeTwo_Option2 = request.form['Option2']
        quesTypeTwo_CorrAnswer = request.form['CorrectAnswer']
        quesType_Two = question(question=quesTypeTwo_Content,
                                difficulty=quesTypeTwo_DifLevel, 
                                value=quesTypeTwo_Point,
                                answer_1=quesTypTwo_Option1, 
                                answer_2=quesTypeTwo_Option2, 
                                correct_answer=quesTypeTwo_CorrAnswer,)
        db.session.add(quesType_Two)
        db.session.commit()
        return redirect(url_for(createQuestion))

        # #   Edit or delete question
        # if request.form['cQ_EDITorDELETE'] == 'EDIT':


    if request.method == 'GET':
        quesTable = db.session.query(question).all()
        global question_Number
        question_Number = db.session.query(question.count(question.id)).scalar()
        global quesTable_Title
        quesTable_Title = db.session.query(question.question).all()
        global quesTable_Points
        quesTable_Points = db.session.query(question.value).all()

    return render_template('createQuestion.html', quesTable_Title=quesTable_Title, quesTable_Points=quesTable_Points,\
                           question_Number=question_Number,)


