from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from AssessmentApp import app, login_manager
from AssessmentApp.forms import LoginForm, RegistrationForm
from AssessmentApp.models import *
from AssessmentApp.routes_RC import *
from AssessmentApp.routes_EK import *
from AssessmentApp.routes_NK import *
#from AssessmentApp.routes_QL import *


@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    User = user.query.filter_by(email=form.email.data).first()
    if User is not None and User.verify_password(form.password.data):
      login_user(User)
      flash('Login successful!')
      return redirect(url_for('staffaccount'))
    flash('Invalid email address or password.')
    return render_template('login.html',form=form)

  return render_template('login.html',title='Login',form=form)
    # testData = test.query.all()

@app.route('/home',methods=['GET','POST'])
def home():
  return render_template('staffaccount.html')

# @app.route('/addQ/<int:id>', methods = ["GET", "POST"])
# def addQ(id):
#     return "Thee Assessment id is " + str(id)

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
  results = assessment_results.query.filter(assessment_results.user_id==current_user.id)

  return render_template('view_assessments.html', assess=assess, id = module_id, results=results )

@app.route("/edit-assessments/<int:assess_id>", methods = ["GET", "POST"])
def edit_assessment(assess_id):
  assess = assessment_details.query.filter(assessment_details.id==assess_id)
  ass = assessment_details.query.filter(assessment_details.id==assess_id).first()
  module = modules.query.filter(modules.id==assessment_details.module_id)
  mod = modules.query.filter(modules.id==assessment_details.module_id).first()
  if request.method == "POST":
      ass.assessment_type = bool(request.form['assType'])
      ass.assessment_name = request.form['assTitle']
      ass.time_limit = datetime.strptime(request.form['assTime'], '%Y-%m-%d %H:%M:%S')
      ass.start_date = datetime.strptime(request.form['assStart'], '%Y-%m-%d %H:%M:%S')
      ass.end_date = datetime.strptime(request.form['assEnd'], '%Y-%m-%d %H:%M:%S')
      ass.release = datetime.strptime(request.form['assRel'], '%Y-%m-%d %H:%M:%S')
      ass.weighting = int(request.form['assWeight'])
      ass.allowed_attemps = int(request.form['assAttemps'])
      ass.assessment_instructions = request.form['assInstruc']

      db.session.commit()
      return redirect(url_for('view_assessments', module_id = mod.id))
    
  return render_template('edit_assessment.html', assess=assess, module=module)

@app.route("/delete-assessments/<int:assess_id>")
def delete_assessment(assess_id):
  assess = assessment_details.query.filter(assessment_details.id==assess_id).first()
  mod = modules.query.filter(modules.id==assessment_details.module_id).first()
  db.session.delete(assess)
  db.session.commit()
  return redirect(url_for('view_assessments', module_id = mod.id))


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

@app.route('/createQuestion')
def createQuestion():
  return render_template('createQuestion.html')


 # return render_template('login.html',form=form)

  #return render_template('login.html',title='Login',form=form)
