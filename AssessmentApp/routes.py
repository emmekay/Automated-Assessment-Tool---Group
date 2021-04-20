from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from AssessmentApp import app, login_manager
from AssessmentApp.forms import LoginForm, RegistrationForm
from AssessmentApp.models import *
from AssessmentApp.routes_RC import *

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    User = user.query.filter_by(email=form.email.data).first()
    if User is not None and User.verify_password(form.password.data):
      login_user(User)
      flash('Login successful!')
      return redirect(url_for('home'))
    flash('Invalid email address or password.')
    return render_template('login.html',form=form)

  return render_template('login.html',title='Login',form=form)
    # testData = test.query.all()

@app.route('/home',methods=['GET','POST'])
def home():
  return render_template('index.html')



"""#@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    User = user.query.filter_by(email=form.email.data).first()
    #if User is not None and User.verify_password(form.password.data):
    login_user(User)
    flash('Login successful!')
    # return
    return redirect("/staffaccount")
    #flash('Invalid email address or password.')

    #return render_template('login.html',form=form)

  return render_template('login.html',title='Login',form=form)
    # testData = test.query.all()

@app.route('/home',methods=['GET','POST'])
def home():
  return render_template('index.html')

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = user.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('Login successful!')
      return redirect(url_for('home'))
    flash('Invalid email address or password.')

    return render_template('login.html',form=form)

  return render_template('login.html',title='Login',form=form)
"""


@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('login'))

@app.route("/view-modules")
def view_modules():
  #enrolled = modules_enrolment.query.all()
  Modules = modules.query.all()
  return render_template('view_modules.html', Modules=Modules)

@app.route("/view-assessments/<int:module_id>")
def view_assessments(module_id):
  assess = assessment_details.query.filter(assessment_details.module_id==module_id)
  return render_template('view_assessments.html', assess=assess)

@app.route("/edit-assessments/<int:assess_id>")
def edit_assessment(assess_id):
  assess = assessment_details.query.filter(assessment_details.id==assess_id)
  return render_template('edit_assessment.html', assess=assess)

@app.route("/survey")
def survey():
    print("Total number of surveys is", survey.query.count())
    return render_template('survey.html', title='Assessment Completed')


@app.route("/staffaccount") # EK
def staffaccount():
    return render_template('staffaccount.html', title='My Account')

@app.route("/studentaccount") # EK
def studentaccount():
    return render_template('studentaccount.html', title='My Account')

@app.route("/surveyresults") # EK
def surveyresults():
    return render_template('surveyresults.html', title='Feedback Summary')


@app.route('/my_assessments') #NK
def my_assessments():
    return render_template('my_assessments.html')

@app.route('/completed_assessments') #NK
def completed_assessments():
    return render_template('completed_assessments.html')

@app.route('/assessment_statistics') #NK
def assessment_statistics():
    return render_template('assessment_statistics.html')

'''
@app.route("/assessment_statistics")
def assessment_stats():
  #enrolled = modules_enrolment.query.all()
  Results = assessment_results.query.all()
  return render_template('assessment_statistics.html', Results=Results)

@app.route("/assessment_statistics/<int:grade>")
def assessment_statistics(grade):
  results = assessment_results.query.filter(assessment_results.grade==grade)
  return render_template('assessment_statistics.html', results=results)

 def Average(grades):
     average=sum(grades)/len(grades)
     return average

 def Lowest(grades):
     grade_list=[]
     grade_list.append(grades)
     low=min(grade_list)
     return low

def Highest(grades):
    grade_list=[]
    grade_list.append(grades)
    high=max(grade_list)
    return high
  '''

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    User = user(username=form.username.data, email=form.email.data, password=form.password.data, first_name=form.first_name.data, last_name=form.last_name.data)
    db.session.add(User)
    db.session.commit()
    flash('Registration Succesful, Please login now.')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

"""@app.route("/delete-assessments/<int:assess_id>")
def delete_assessment(assess_id,module_id):
  assess = assessment_details.query.filter(assessment_details.id==assess_id)
  db.session.delete(assess)
  db.session.commit()
  assess = assessment_details.query.filter(assessment_details.module_id==module_id)
  return render_template('view_assessments_staff.html',assess=assess)"""


 # return render_template('login.html',form=form)

  #return render_template('login.html',title='Login',form=form)
