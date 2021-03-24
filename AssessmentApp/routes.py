from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/')
def index():
    # testData = test.query.all()

    return render_template('index.html')#, test1 = testData)


@app.route('/addAss')
def addAss():
    # testData = test.query.all()

    return render_template('AssessmentDetails.html')#, test1 = testData)

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('Login successful!')
      return redirect(url_for('home'))
    flash('Invalid email address or password.')
    
    return render_template('login.html',form=form)

  return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('login'))