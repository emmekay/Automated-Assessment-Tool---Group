# from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from AssessmentApp import db
from datetime import datetime



class test(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(30))

class AssessmentDetails(db.Model):
    id = db.Column(db.Integer , primary_key = True)
<<<<<<< HEAD
    moduleId = db.Column(db.String(10), nullable=False) #WILL CHANGE TO FORIGNE KEY WHEN TABLE MADE
    allowedAttemps = db.Column(db.Integer, default = 100)
    weighting = db.Column(db.Integer , nullable=False)
    timeLimit =  db.Column(db.DateTime, nullable=False)
    release =  db.Column(db.DateTime, nullable=False)
    end =  db.Column(db.DateTime, nullable=False)
    start =  db.Column(db.DateTime, nullable=False)
    studentInstructions = db.Column(db.Text())
=======
    module_Id = db.Column(db.String(10), nullable=False) #WILL CHANGE TO FORIGNE KEY WHEN TABLE MADE
    allowed_Attemps = db.Column(db.Integer, default = 100)
    weighting = db.Column(db.Integer , nullable=False)
    time_Limit =  db.Column(db.DateTime, nullable=False)
    # release =  db.Column(db.DateTime, nullable=False)
    end =  db.Column(db.DateTime, nullable=False)
    start =  db.Column(db.DateTime, nullable=False)
    student_Instructions = db.Column(db.Text())
>>>>>>> 04e4a839743f31f56690a8c45d599a8af359d831

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

#Emilia's Class
class Student(db.Model): #Student Info
    id = db.Column(db.Integer, primary_key=True)
    modules = db.relationship('Modules', backref='module_parent', lazy='dynamic')

class Staff(db.Model): # Staff Info
    id = db.Column(db.Integer, primary_key=True)
    staff_surname = db.Column(db.String(64), index=True, unique=False)
    modules = db.relationship('Modules', backref='instructor', lazy='dynamic')

<<<<<<< HEAD
class Satisfaction(db.Model): #Satisfaction Survey - Completely confused on this one 
    id = db.Column(db.Integer, primary_key=True)
    assessment_id =  db.relationship('AssessmentDetails', backref=module, lazy='dynamic')
    question_one = 
    question_two =
    question_three =
    question_four =
    question_five =

class Modules(db.Model): #statistics
    id = db.Column(db.Integer , primary_key = True) 
    module_id = db.Column(db.String(10))
    module_name = db.Column(db.String(40))
    module_leader = db.Column(db.String(30))
=======

class Satisfaction(db.Model): #Satisfaction Survey - Completely confused on this one
    id = db.Column(db.Integer, primary_key=True)
    assessment_id =  db.relationship('AssessmentDetails', backref=module, lazy='dynamic')
    question_one =
    question_two =
    question_three =
    question_four =
    question_five = 


class Assessment_Results(db.Model):
    student_id = db.relationship('Student', backref=module, lazy='dynamic', primary_key=True)
    assessment_id = db.relationship('AssessmentDetails', backref=module, lazy='dynamic', primary_key=True)
    grade = db.Column(db.Integer)
    no_of_attempts = db.Column(db.Integer)
>>>>>>> 04e4a839743f31f56690a8c45d599a8af359d831
