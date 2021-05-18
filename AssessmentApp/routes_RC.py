from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from datetime import datetime

from AssessmentApp import app
from AssessmentApp.models import *
from AssessmentApp.forms_RC import *


@app.route('/addAssessment/<int:id>' , methods = ["GET", "POST"])
@login_required
def addAssessment(id):
    form = AsseDetails()

    if request.method == "POST":

        Inval = False
        if form.aWeight.data == None:
            flash("Weighting must be between 0-100")
            Inval = True
        if form.aAttemps.data == None:
            flash("Attempts must be between 1-100")
            Inval = True
        if form.aEnd.data <= form.aStart.data:
            flash("Start Date must be before End Date")
            Inval = True

        if Inval == True:
            return redirect(url_for('addAssessment', id = id))



        module_id = id # request.form['module']

        if form.aType.data == '0':
            assessment_type = False
        else:
            assessment_type = True


        assessment_name = form.aTitle.data
        time_limit =datetime.combine( form.aStart.data, form.aTimeAva.data)
        time_limit.date()
        # print(type(time_limit))
        start_date = datetime.combine( form.aStart.data , form.aStartTime.data)

        end_date = datetime.combine( form.aEnd.data , form.aEndTime.data)
        # print(end_date)
        release = datetime.combine( form.aRel.data , form.aRelTime.data)

        weighting = int(form.aWeight.data)
        allowed_attemps = int(form.aAttemps.data)
        if weighting >100 or weighting <0:
            flash("Invalid Input- Weighting must be between 1-100")
            Inval = True

        if allowed_attemps >100 or allowed_attemps <0:
            flash("Invalid Input- Attempts must be between 1-100")
            Inval = True


        assessment_instructions = form.aDes.data


        if Inval == True:
            return redirect(url_for('addAssessment', id = id))

        ass = assessment_details(module_id = module_id, assessment_type = assessment_type, assessment_name = assessment_name, time_limit = time_limit, start_date = start_date, end_date = end_date, release = release, weighting = weighting, allowed_attemps = allowed_attemps,  assessment_instructions = assessment_instructions)


        db.session.add(ass)
        db.session.commit()


        flash("Assessment Successfully Created")
        return redirect(url_for('view_assessments', module_id = id))


    return render_template('AssessmentDetails.html', id = id, form = form)


@app.route('/assessment/<int:id>', methods = ["GET", "POST"])
@login_required
def assessment(id):
    ass = assessment_details.query.filter_by(id=id).first()
    questionIds = assessment_questions.query.filter_by(assessment_id=id).all()
    assQuestions = [ question.query.filter_by(id=q.question_id).first() for q in questionIds]
    prev = assessment_results.query.filter_by(assessment_id=id, user_id = current_user.id).all()

    inAttemptRange = ass.allowed_attemps <= len(prev)

    outDateRange = [False,False]
    if ass.start_date <= datetime.utcnow():
        outDateRange[0] = True
    if ass.end_date >= datetime.utcnow():
        outDateRange[1] = True


    if request.method == "POST":

        correct = 0
        totalPossibleMarks = 0

        res1 = {}
        ans = {}

        res4 = ""
        myAnswer = ""

        for i, q in enumerate (assQuestions):#
            totalPossibleMarks += q.value

            # Save answer
            if q.correct_answer:
                ans[q.id] = getattr(q, "answer_"+ str(request.form['Q' +str(q.id)])) , getattr(q, "answer_"+ str(q.correct_answer))
            else:
                ans[q.id] = str(request.form['Q' +str(q.id)]) , str(q.type_2_answer)


            if q.correct_answer and request.form['Q' +str(q.id)] == str(q.correct_answer):
                correct += q.value
                res1[q.id] = True

                res4 += "1"
                myAnswer += request.form['Q' +str(q.id)] + ","
            elif (not q.correct_answer) and request.form['Q' +str(q.id)] == str(q.type_2_answer):
                correct += q.value
                res1[q.id] = True
                res4 += "1"
                myAnswer += request.form['Q' +str(q.id)] + ","
            else:
                res1[q.id] = False
                res4 += "0"
                myAnswer += request.form['Q' +str(q.id)] + ","

        myAnswer = myAnswer[:-1]

        #IF FORMATIVE
        isFormative = False

        if ass.assessment_type == 0:
            isFormative = True
            flash(str(correct) + "/" + str(totalPossibleMarks) + " Marks")
        else:
            flash("This Assessment is Summative, no instant results available. ")

        if (len(assQuestions) > 0 and not current_user.is_staff):
            att = assessment_results.query.filter_by(user_id = current_user.id, assessment_id = id).all()
            res = assessment_results(user_id = current_user.id, assessment_id = id, attempt_number = len(att)+1, grade = round((correct/totalPossibleMarks)*100), date_completed = datetime.now(), result_string = res4, answer_string = myAnswer)
            db.session.add(res)
            db.session.commit()


        return render_template('Confi.html', ass = ass, assQuestions =assQuestions, res1 =res1, isFormative = isFormative, myAnswer = myAnswer, ans = ans)

    return render_template('UndertakeAssessment.html',  assQuestions =assQuestions, ass = ass, id = id, outDateRange = outDateRange, inAttemptRange = inAttemptRange, totalQ = len(assQuestions))


@app.route('/editAssessment/<int:a_id>' , methods = ["GET", "POST"])
@login_required
def editAssessment(a_id):
    form = AsseDetails()
    assess = assessment_details.query.filter_by(id=a_id).first()
    id = assess.module_id
    oldTimeLimit = assess.time_limit.strftime("%H:%M")
    oldStart = [assess.start_date.strftime("%Y-%m-%d"), assess.start_date.strftime("%H:%M")]
    oldEnd = [assess.end_date.strftime("%Y-%m-%d"), assess.end_date.strftime("%H:%M")]
    oldRel = [assess.release.strftime("%Y-%m-%d"), assess.release.strftime("%H:%M")]
    a_type = int(assess.assessment_type)
    mod = modules.query.filter_by(id = id).first()



    if request.method == "POST":
        Inval = False
        if form.aWeight.data == None:
            flash("Weighting must be between 0-100")
            Inval = True
        if form.aAttemps.data == None:
            flash("Attempts must be between 1-100")
            Inval = True
        if form.aEnd.data <= form.aStart.data:
            flash("Start Date must be before End Date")
            Inval = True
        if Inval == True:
            return redirect(url_for('editAssessment', a_id = a_id))



        # module_id = id # request.form['module']

        if form.aType.data == '0':
            assessment_type = False
        else:
            assessment_type = True

        assessment_name = form.aTitle.data
        time_limit =datetime.combine( form.aStart.data, form.aTimeAva.data)
        time_limit.date()
        start_date = datetime.combine( form.aStart.data , form.aStartTime.data)
        end_date = datetime.combine( form.aEnd.data , form.aEndTime.data)
        assessment_instructions = form.aDes.data
        release = datetime.combine( form.aRel.data , form.aRelTime.data)
        weighting = int(form.aWeight.data)
        allowed_attemps = int(form.aAttemps.data)
        if weighting >100 or weighting <0:
            flash("Invalid Input- Weighting must be between 1-100")
            Inval = True
        if allowed_attemps >100 or allowed_attemps <0:
            flash("Invalid Input- Attempts must be between 1-100")
            Inval = True
        if Inval == True:
            return redirect(url_for('editAssessment', a_id = a_id))

        assess.assessment_type = assessment_type
        assess.assessment_name = assessment_name
        assess.time_limit = time_limit
        assess.end_date = end_date
        assess.start_date = start_date
        assess.release = release
        assess.allowed_attemps = allowed_attemps
        assess.weighting = weighting
        assess.assessment_instructions = assessment_instructions

        db.session.commit()


        flash("Assessment Successfully Modified")
        return redirect(url_for('view_assessments', module_id = id))


    return render_template('EditAssessmentDetails.html',
    a_id= a_id,
    form = form,
    assess = assess,
    mod = mod,
    oldTimeLimit = oldTimeLimit,
    oldStart = oldStart, oldEnd =oldEnd,
    oldRel = oldRel,
    a_type = a_type)
