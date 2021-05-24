from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from statistics import mean

from AssessmentApp import app, db
from AssessmentApp.models import *


@app.route("/my_assessments/<int:user_id>")
def my_assessments(user_id):

    # Pulling all assessment results for the current user
    result_ids = assessment_results.query.filter_by(user_id=current_user.id).all()
    num_of_assessments = len(result_ids)

    # Storing all modules that the curent user is enrolled in in a dictionary
    Modules = modules_enrolment.query.filter_by(user_id=current_user.id).all()
    enrolled_mod = []
    mod_names = {}
    for m in Modules:
        enrolled_mod.append(m.module_id)
        mod_names[m.module_id] = (
            modules.query.filter_by(id=m.module_id).first().module_name
        )

    # Storing all assessments for the specific modules in a dictionary
    Assessments = {}
    Assessments_id = []
    for m_id in enrolled_mod:
        temp = []
        Assess_details = assessment_details.query.filter_by(module_id=m_id).all()

        for a in Assess_details:
            temp.append(a)
            Assessments_id.append(a.id)

        Assessments[m_id] = temp

    # Storing the last attempt of an assessment's result in a dictionary
    # Assess_results = {}
    # for a_id in Assessments_id:
    #     temp_a = assessment_results.query.filter_by(
    #         assessment_id=a_id, user_id=current_user.id
    #     ).all()
    #     if temp_a:
    #         Assess_results[a_id] = temp_a[-1].grade

    Assess_results = {}
    for a_id in Assessments_id:
        user_results = assessment_results.query.filter_by(
            assessment_id=a_id, user_id=current_user.id
        ).all()

        all_attempts = []
        for result in user_results:
            all_attempts.append(result.grade)
            attempts_average = round((sum(all_attempts) / len(all_attempts)), 1)

        if user_results:
            Assess_results[a_id] = attempts_average

    return render_template(
        "my_assessments.html",
        result_ids=result_ids,
        num_of_assessments=num_of_assessments,
        enrolled_mod=enrolled_mod,
        Assessments=Assessments,
        Assess_results=Assess_results,
        mod_names=mod_names,
    )


@app.route("/completed_assessments/<int:user_id>")
def completed_assessments(user_id):

    # Pulling all assessment results for the current user, notice we use filter_by() instead of .filter()
    result_ids = assessment_results.query.filter_by(user_id=current_user.id).all()

    # Declaring list containing assessment IDs
    assess_id = []
    # Declaring dictionary containing assessment details for assessment details & assessment results link
    assess_details = {}

    # Adding all assessment ids to list
    for r in result_ids:
        if r.assessment_id not in assess_id:
            assess_id.append(r.assessment_id)

    # Linking assessment details to assessment results using assess_id
    for a_id in assess_id:
        temp = assessment_details.query.filter_by(id=a_id).first()
        assess_details[a_id] = temp

    assess_id.sort()
    return render_template(
        "completed_assessments.html",
        result_ids=result_ids,
        assess_details=assess_details,
    )


@app.route(
    "/assessment_statistics/<int:assess_id>/<int:id_assessment>"
)  # /ID of the assessment/ID of the assessment result
def assessment_statistics(assess_id, id_assessment):

    # Pulling individual student's results for this assessment based off user ID & assessment result ID
    user_results = assessment_results.query.filter_by(
        user_id=current_user.id, assessment_id=assess_id, id=id_assessment
    ).first()

    # Pulling all of class results for this assessment from db
    class_results = assessment_results.query.filter_by(assessment_id=assess_id).all()

    # Pulling assesment details based on assessment id
    assess_details = assessment_details.query.filter_by(id=assess_id).first()

    # Pulling module details based on assessment id
    module_details = modules.query.filter_by(id=assess_details.module_id).first()

    all_grades = []
    for result in class_results:
        all_grades.append(result.grade)
    class_average = round((sum(all_grades) / len(all_grades)), 1)

    # Getting lowest grade
    lowest_grade = min(all_grades)

    # Getting highest grade
    highest_grade = max(all_grades)

    return render_template(
        "assessment_statistics.html",
        user_results=user_results,
        module_details=module_details,
        assess_details=assess_details,
        class_average=class_average,
        lowest_grade=lowest_grade,
        highest_grade=highest_grade,
    )

    # ----- OLD COMPLETED ASSESSMENT CODE -----
    # for(r in res):
    #     print(r.grade)

    # print(res[0].grade)
    # assessments = (
    #     db.session.query(
    #         assessment_details, modules_enrolment, assessment_results
    #     ).filter(
    #         assessment_results.user_id == current_user.id
    #         and assessment_results.user_id == modules_enrolment.user_id
    #         and modules_enrolment.module_id == assessment_details.module_id
    #     )
    # ).all()

    # ------OLD CODE FOR ASSESSMENT STATISTICS ------
    # module = modules.query.filter(
    #     modules.module_id == assess_id
    # ).first()  # Need to link tables here
    # assname = assessment_details.query.filter(
    #     assessment_details.module_id == assess_id
    # ).first()
    # attempt = assessment_results.query.filter(
    #     assessment_results.assessment_id == assess_id
    # ).first()
    # results = assessment_results.query.filter(
    #     assessment_results.assessment_id == assess_id
    # )
    # return render_template(
    #     "assessment_statistics.html",
    #     Results=results,
    #     Module=module,
    #     Assname=assname,
    #     Attempt=attempt,
    # )


# ----------------------------- OLD ASSESSMENT STATS CODE FOR PULLING MODULE NAME ---------------------------
# ass_id = []
# #
# assess_details = {}
#
# #
# for m in module_details:
#     if m.module_id not in ass_id:
#         ass_id.append(m.module_id)
#
# # Linking assessment details to assessment results using assess_id
# for m_id in ass_id:
#     #
#     temp = assessment_details.query.filter_by(id=m_id).first()
#     assess_details[m_id] = temp

# Calculating class average using all grades from the assessment limited to 1 decimal place
