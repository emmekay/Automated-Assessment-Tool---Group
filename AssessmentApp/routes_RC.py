from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from AssessmentApp import app
from AssessmentApp.models import *

@app.route('/addAss/<int:id>' , methods = ["GET", "POST"])
def addAss(id):
    if request.method == "POST":
        module_id = id # request.form['module']
        assessment_type = bool(request.form['assType'])
        assessment_name = request.form['assTitle']
        time_limit = datetime.strptime(request.form['assTime'], '%H:%M')
        start_date = datetime.strptime(request.form['assStart'] +" "+ request.form['assStartTime'], '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(request.form['assEnd'] +" "+ request.form['assEndTime'], '%Y-%m-%d %H:%M')
        release = datetime.strptime(request.form['assRel'] +" "+ request.form['assRelTime'], '%Y-%m-%d %H:%M')
        # assMarks = int(request.form['assMarks'])
        weighting = int(request.form['assWeight'])
        allowed_attemps = int(request.form['assAttemps'])
        assessment_instructions = request.form['assInstruc']




        # print(assType)
        ass = assessment_details(module_id = module_id, assessment_type = assessment_type, assessment_name = assessment_name, time_limit = time_limit, start_date = start_date, end_date = end_date, release = release, weighting = weighting, allowed_attemps = allowed_attemps,  assessment_instructions = assessment_instructions)
        db.session.add(ass)
        db.session.commit()

        redirect(url_for('view_assessments', module_id = id))


    return render_template('AssessmentDetails.html', id = id)

@app.route('/assessment/<int:id>', methods = ["GET", "POST"])
def Ass(id):
    ass = assessment_details.query.filter_by(id=id).first()
    questionIds = assessment_questions.query.filter_by(assessment_id=id).all()

    assQuestions = [ question.query.filter_by(id=q.question_id).first() for q in questionIds]
    # current_user.id
    prev = assessment_results.query.filter_by(assessment_id=id, user_id = current_user.id).all()
    if (len(prev) >= ass.allowed_attemps):
        flash("You have exceeded the toal numebr of attempts" )
    # TEMP
    outDateRange = [0,0]
    if ass.start_date < datetime.utcnow():
        outDateRange[0] = 1
    if ass.end_date > datetime.utcnow():
        outDateRange[1] = 1


    # Temp END
    if request.method == "POST":
        correct = 0
        totalPossibleMarks = 0
        res1 = {}
        for i, q in enumerate (assQuestions):#
            totalPossibleMarks += q.value
            if q.correct_answer and request.form['Q' +str(q.id)] == str(q.correct_answer):
                correct += q.value
                res1[q.id] = True
            elif (not q.correct_answer) and request.form['Q' +str(q.id)] == str(q.type_2_answer):
                correct += q.value
                res1[q.id] = True
            else:
                res1[q.id] = False



        #IF FORMATIVE
        if not ass.assessment_type:
            flash(str(correct) + "/" + str(totalPossibleMarks) + " Marks")
        else:
            flash("This Assessment is Sumative, no instant results avialible. ")
            
        att = assessment_results.query.filter_by(user_id = current_user.id, assessment_id = id).all()
        res = assessment_results(user_id = current_user.id, assessment_id = id, attempt_number = len(att)+1, grade = round((correct/totalPossibleMarks)*100), date_completed = datetime.now())
        db.session.add(res)
        db.session.commit()


        return render_template('Confi.html', ass = ass, assQuestions =assQuestions, res1 =res1)
        # return redirect(url_for('confirmation', id = id))



    return render_template('UndertakeAss.html',  assQuestions =assQuestions, ass = ass, id = id, outDateRange = outDateRange)



@app.route('/confirmation/<int:id>', methods = ["GET", "POST"])
def confirmation(id):
    ass = assessment_details.query.filter_by(id=id).first()

    questionIds = assessment_questions.query.filter_by(assessment_id=id).all()

    assQuestions = [ question.query.filter_by(id=q.question_id).first() for q in questionIds]


    return render_template('Confi.html', ass = ass, assQuestions =assQuestions)
