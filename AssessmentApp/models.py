# from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from AssessmentApp import db
from datetime import datetime



class test(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(30))

class AssessmentDetails(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    moduleId = db.Column(db.String(10), nullable=False) #WILL CHANGE TO FORIGNE KEY WHEN TABLE MADE
    allowedAttemps = db.Column(db.Integer, default = 100)
    weighting = db.Column(db.Integer , nullable=False)
    timeLimit =  db.Column(db.DateTime, nullable=False)
    release =  db.Column(db.DateTime, nullable=False)
    end =  db.Column(db.DateTime, nullable=False)
    start =  db.Column(db.DateTime, nullable=False)
    studentInstructions = db.Column(db.Text())

class QuestionTypeTwo(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False) #Standard answers provided by teaching staff
    level = db.Column(db.Integer, nullable=False) #Question defficulty levels
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)

class QuestionTwoAnswer(db.Model):
    id = db.Column(db.Integer, Primary_key = True)
    answer = db.Column(db.Text, nullable=False) #Student's answers
    question_id = db.Column(db.Integer, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    parent_id = db.Column(db.Interger, db.ForeignKey('QuestionTwoAnswer.id'), nullable=True)
    parent = db.relationship('QuestionTwoAnswer', backref='questiontwoanswer_parent', remote_side=id, lazy=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, Primary_key = True)
    concent = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    parent_id = db.Column(db.Interger, db.ForeignKey('Feedback.id'), nullable=True)
    parent = db.relationship('QuestionTwoAnswer', backref='feedback_parent', remote_side=id, lazy=True)


class Tag(db.Model): #Question type two tags
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(32), unique=True, index=True, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('staff.id'),nullable=False)
    question_id = db.Column(db.Interger, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    parent_id = db.Column(db.Interger, db.ForeignKey('Tag.id'), nullable=True)
    parent = db.relationship('Tag', backref='tag_parent', remote_side=id, lazy='dynamic')

class Point(db.Model): #Question type two points
    id = db.Column(db.Interger, primary_key=True)
    point = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer,db.ForeignKey('staff.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    parent_id = db.Column(db.Interger, db.ForeignKey('Point.id'), nullable=True)
    parent = db.relationship('Point', backref='point_parent', remote_side=id, lazy=True)