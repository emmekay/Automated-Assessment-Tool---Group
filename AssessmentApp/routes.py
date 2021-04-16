from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


from flask_login import login_user, logout_user, login_required, current_user
from AssessmentApp import app, db#, login_manager
from AssessmentApp.forms import LoginForm
from AssessmentApp.models import *


@app.route('/')
def index():
    #testData = test.query.all()
    return render_template('index.html')#, test1 = testData)


@app.route('/addAss', methods=["GET", "POST"])
def addAss():
    if request.method == "POST":
        module_id = request.form['module']
        assessment_type = bool(request.form['assType'])
        assessment_name = request.form['assTitle']
        time_limit = datetime.strptime(request.form['assTime'], '%H:%M')
        start_date = datetime.strptime(
            request.form['assStart'] + " " + request.form['assStartTime'], '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(
            request.form['assEnd'] + " " + request.form['assEndTime'], '%Y-%m-%d %H:%M')
        release = datetime.strptime(
            request.form['assRel'] + " " + request.form['assRelTime'], '%Y-%m-%d %H:%M')
        # assMarks = int(request.form['assMarks'])
        weighting = int(request.form['assWeight'])
        allowed_attemps = int(request.form['assAttemps'])
        assessment_instructions = request.form['assInstruc']

        # print(assType)
        ass = assessment_details(module_id=module_id, assessment_type=assessment_type, assessment_name=assessment_name, time_limit=time_limit, start_date=start_date,
                                 end_date=end_date, release=release, weighting=weighting, allowed_attemps=allowed_attemps,  assessment_instructions=assessment_instructions)
        db.session.add(ass)
        db.session.commit()

    return render_template('AssessmentDetails.html')



@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    User = user.query.filter_by(email=form.email.data).first()
    #if User is not None and User.verify_password(form.password.data):
    login_user(User)
    flash('Login successful!')
    return redirect(url_for('home'))
    #flash('Invalid email address or password.')
    
    #return render_template('login.html',form=form)

  return render_template('login.html',title='Login',form=form)
    # testData = test.query.all()

"""@app.route('/home',methods=['GET','POST'])
def home():
  return render_template('index.html')

@app.route('/addAss')
def addAss():
    # testData = test.query.all()

    return render_template('AssessmentDetails.html')#, test1 = testData)"""


@app.route('/assessment/<int:id>', methods=["GET", "POST"])
def Ass(id):

    ass = assessment_details.query.filter_by(id=id).first()

    questionIds = assessment_questions.query.filter_by(assessment_id=id).all()

    assQuestions = [question.query.filter_by(
        id=q.question_id).first() for q in questionIds]

    if request.method == "POST":
        correct = 0
        totalPossibleMarks = 0
        for i, q in enumerate(assQuestions):
            totalPossibleMarks += q.value
            if q.correct_answer and request.form['Q' + str(q.id)] == str(q.correct_answer):
                correct += q.value
            elif (not q.correct_answer) and request.form['Q' + str(q.id)] == str(q.type_2_answer):
                correct += q.value
        flash(str(correct) + "/" + str(totalPossibleMarks) + " Marks")

    return render_template('UndertakeAss.html',  assQuestions=assQuestions, ass=ass, id=id)




"""@app.route("/login",methods=['GET','POST'])
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


@app.route("/survey", methods=['GET', 'POST'])
def survey():
    form = Survey()
    if form.validate_on_submit():
        user = Survey(user_id=current_user.id, assessment_id=form.assessment_id.data,
                      question_1=form.question_1.data, question_2=form.question_1.data, question_3=form.question_1.data, question_4=form.question_1.data)
        db.session.add(user)
        db.session.commit()
        flash('Survey Submitted')
        return redirect(url_for('index.html'))
    return render_template('survey.html', title='Survey', form=form)


"""@app.route("/survey", methods=["GET"])
def survey():
  if request.method == 'GET':
    question_1 = request.args.get('question_1')
    query_string="?question_1={0}".format(question_1)
    return render_template('survey.html', query_string=query_string, title='Assessment Completed')"""

@app.route("/staffaccount") # EK
def staffaccount():
    return render_template('staffaccount.html', title='My Account')

@app.route("/studentaccount") # EK
def studentaccount():
    return render_template('studentaccount.html', title='My Account')

@app.route("/surveyresults") # EK 
def surveyresults():
    return render_template('surveyresults.html', title='Feedback Summary')


@app.route('/my_assessments')
def my_assessments():
    return render_template('my_assessments.html')


@app.route('/completed_assessments')
def completed_assessments():
    return render_template('completed_assessments.html')


@app.route('/assessment_statistics')
def assessment_statistics():
    return render_template('assessment_statistics.html')






"""@app.route("/delete-assessments/<int:assess_id>")
def delete_assessment(assess_id,module_id):
  assess = assessment_details.query.filter(assessment_details.id==assess_id)
  db.session.delete(assess)
  db.session.commit()
  assess = assessment_details.query.filter(assessment_details.module_id==module_id)
  return render_template('view_assessments_staff.html',assess=assess)"""


 # return render_template('login.html',form=form)

  #return render_template('login.html',title='Login',form=form)

"""@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('login'))"""
