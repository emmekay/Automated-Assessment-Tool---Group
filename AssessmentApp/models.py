# from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from AssessmentApp import db


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
