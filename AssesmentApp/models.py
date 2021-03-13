# from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from AssesmentApp import db

class StudentUsers(db.Model):
    studentId = db.Column(db.String(20) , primary_key = True)
    FamilyName = db.Column(db.String(30))
    GivenName = db.Column(db.String(30))
    Department = db.Column(db.String(30))
    Programme = db.Column(db.String(30))
