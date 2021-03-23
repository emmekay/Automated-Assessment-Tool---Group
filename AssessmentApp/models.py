# from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from AssessmentApp import db#, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class test(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(30))

class user(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    last_name = db.Column(db.String(40), unique = False, nullable = False)
    first_name = db.Column(db.String(40), unique = False, nullable = False)
    username = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable = False)
    is_staff = db.Column(db.Boolean, default = False, nullable = False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

#@login_manager.user_loader
#def load_user(user_id):
#  return user.query.get(int(user_id))

class modules(db.Model): #statistics
    id = db.Column(db.Integer , primary_key = True) 
    module_id = db.Column(db.String(10), unique = True, nullable = False)
    module_name = db.Column(db.String(40), nullable = False)
    module_leader = db.Column(db.String(30))

class modules_enrolment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))

class assessment_details(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id')) 
    allowed_attemps = db.Column(db.Integer, default = 100)
    weighting = db.Column(db.Integer , nullable=False)
    time_limit =  db.Column(db.DateTime, nullable=False)
    release =  db.Column(db.DateTime, nullable=False)
    end_date =  db.Column(db.DateTime, nullable=False)
    start_date =  db.Column(db.DateTime, nullable=False)

class assessment_results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment_details.id'))
    attempt_number = db.Column(db.Integer, nullable = False)
    grade = db.Column(db.Integer, nullable = False)
    date_completed = db.Column(db.DateTime, nullable=False)
    student_instructions = db.Column(db.Text())

class Modules(db.Model): #statistics
    id = db.Column(db.Integer , primary_key = True)
    module_id = db.Column(db.String(10))
    module_name = db.Column(db.String(40))
    module_leader = db.Column(db.String(30))

class assessment_results(db.Model):
    attempt_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.relationship('Student', backref='Student', lazy='dynamic')
    assessment_id = db.relationship('AssessmentDetails', backref='Modules', lazy='dynamic')
    attempt_number = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    date_completed = db.Column(db.DateTime, nullable=False)
    no_of_attempts = db.Column(db.Integer)
    no_of_attempts = db.Column(db.Integer)
