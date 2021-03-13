from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from AssesmentApp import app
from AssesmentApp.models import *

@app.route('/')
def index():
    testData = test.query.all()

    return render_template('index.html', test1 = testData)
