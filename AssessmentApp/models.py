# from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from AssessmentApp import db
from datetime import datetime

class test(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(30))

class user(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    last_name = db.Column(db.String(40), unique = False, nullable = False)
    first_name = db.Column(db.String(40), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable = False)
    is_staff = db.Column(db.Boolean, default = False, nullable = False)

class modules(db.Model): #statistics
    id = db.Column(db.Integer , primary_key = True) 
    module_id = db.Column(db.String(10), unique = True, nullable = False)
    module_name = db.Column(db.String(40), nullable = False)
    module_leader = db.Column(db.String(30))

class modules_enrolment(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))

class assessment_details(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id')) 
    allowed_attemps = db.Column(db.Integer, default = 100)
    weighting = db.Column(db.Integer , nullable=False)
    timeLimit =  db.Column(db.DateTime, nullable=False)
    release =  db.Column(db.DateTime, nullable=False)
    end =  db.Column(db.DateTime, nullable=False)
    start =  db.Column(db.DateTime, nullable=False)
    student_instructions = db.Column(db.Text())

class assessment_results(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment_details.id'))
    attempt_number = db.Column(db.Integer, nullable = False)
    grade = db.Column(db.Integer, nullable = False)
    date_completed = db.Column(db.DateTime, nullable=False)

class assessment_questions(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment_details.id'))
    question_type = db.Column(db.Boolean, default = False, nullable = False)

class question(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    value = db.Column(db.Integer, nullable = False)
    difficulty = db.Column(db.Integer, nullable = False)
    question = db.Column(db.Text(), nullable = False)
    answer_1 = db.Column(db.Text(), nullable = True)
    answer_2 = db.Column(db.Text(), nullable = True)
    answer_3 = db.Column(db.Text(), nullable = True)
    answer_4 = db.Column(db.Text(), nullable = True)
    correct_answer = db.Column(db.Integer, nullable = True)
    type_2_answer = db.Column(db.Boolean, nullable = True)
    correct_feedback = db.Column(db.Text(), nullable = False)
    incorrect_feedback = db.Column(db.Text(), nullable = False)

class survey(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment_details.id'))
    question_1 = db.Column(db.Integer, nullable = False)
    question_2 = db.Column(db.Integer, nullable = False)
    question_3 = db.Column(db.Integer, nullable = False)
    question_4 = db.Column(db.Integer, nullable = False)

"""class Student(db.Model): #Student Info
    id = db.Column(db.Integer, primary_key=True)
    modules = db.relationship('Modules', backref='module_parent', lazy='dynamic')
    # Student name
    # Student email
    # Passords
    # Programme

class Staff(db.Model): # Staff Info
    id = db.Column(db.Integer, primary_key=True)
    staff_surname = db.Column(db.String(64), index=True, unique=False)
    modules = db.relationship('Modules', backref='instructor', lazy='dynamic')
    # Same with staff



class QuestionTypeTwo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False) #Standard answers provided by teaching staff
    level = db.Column(db.Integer, nullable=False) #Question defficulty levels
    # date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    weighting = db.Column(db.Integer, nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment_details.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)



class QuestionTwoAnswer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    answer = db.Column(db.Text, nullable=False) #Student's answers
    question_id = db.Column(db.Integer, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('QuestionTwoAnswer.id'), nullable=True)
    parent = db.relationship('QuestionTwoAnswer', backref='questiontwoanswer_parent', remote_side=id, lazy=True)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    concent = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('Feedback.id'), nullable=True)
    parent = db.relationship('QuestionTwoAnswer', backref='feedback_parent', remote_side=id, lazy=True)


class Tag(db.Model): #Question type two tags
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(32), unique=True, index=True, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('staff.id'),nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('Tag.id'), nullable=True)
    parent = db.relationship('Tag', backref='tag_parent', remote_side=id, lazy='dynamic')

class Point(db.Model): #Question type two points
    id = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer,db.ForeignKey('staff.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('QuestionTypeTwo.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('Point.id'), nullable=True)
    parent = db.relationship('Point', backref='point_parent', remote_side=id, lazy=True)

#Emilia's Class

    



class Satisfaction(db.Model): #Satisfaction Survey - Completely confused on this one 
    id = db.Column(db.Integer, primary_key=True)
    assessment_id =  db.relationship('AssessmentDetails', backref='Modules', lazy='dynamic')
    #question_one = 
    #question_two =
    #question_three =
    #question_four =
    #question_five =



#class Satisfaction(db.Model): #Satisfaction Survey - Completely confused on this one
#    id = db.Column(db.Integer, primary_key=True)
#    assessment_id =  db.relationship('AssessmentDetails', backref=module, lazy='dynamic')
#    question_one =
#    question_two =
#    question_three =#
#    question_four =
#    question_five = 

"""