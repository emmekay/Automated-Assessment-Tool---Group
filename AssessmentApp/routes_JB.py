from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/module_records')
def module_records():
    return render_template('module_records.html')

@app.route('/course_records')
def course_records():
    return render_template('course_records.html')
