# from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from AssessmentApp import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from AssessmentApp import login_manager


class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(40), unique=False, nullable=False)
    first_name = db.Column(db.String(40), unique=False, nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(60))
    is_staff = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def has_enrolled(self, module):
        return (
            modules_enrolment.query.filter(
                modules_enrolment.user_id == self.id,
                modules_enrolment.module_id == module.id,
            ).count()
            > 0
        )


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class modules(db.Model):  # statistics
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.String(10), unique=True, nullable=False)
    module_name = db.Column(db.String(40), nullable=False)
    module_leader = db.Column(
        db.String(30)
    )  # MAKE FOREIGN KEY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class modules_enrolment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id")
    )  # , db.ForeignKey('user.id'))
    module_id = db.Column(
        db.Integer, db.ForeignKey("modules.id")
    )  # , db.ForeignKey('modules.module_id'))


class assessment_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(
        db.Integer, db.ForeignKey("modules.id")
    )  # , db.ForeignKey('modules.module_id'))
    assessment_type = db.Column(
        db.Boolean, nullable=False
    )  # summative = 0, formative = 1
    assessment_name = db.Column(db.Text, nullable=False)
    assessment_instructions = db.Column(db.Text, nullable=False)
    allowed_attemps = db.Column(db.Integer, default=100)
    weighting = db.Column(db.Integer, nullable=False)
    time_limit = db.Column(db.DateTime, nullable=False)
    release = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)

    # ondelete='CASCADE'


class assessment_results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    assessment_id = db.Column(db.Integer, db.ForeignKey("assessment_details.id"))
    attempt_number = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    date_completed = db.Column(db.DateTime, nullable=False)
    result_string = db.Column(
        db.Text, nullable=True
    )  # string to hold if each quesiton is right or wrong
    answer_string = db.Column(db.Text, nullable=True)
    # passive_deletes=True


class assessment_questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    assessment_id = db.Column(db.Integer, db.ForeignKey("assessment_details.id"))
    question_type = db.Column(
        db.Boolean, nullable=False
    )  # 0 = true/false, 1 = multiple choice

    # passive_deletes=True


class question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    question = db.Column(db.Text(), nullable=False)
    answer_1 = db.Column(db.Text(), nullable=True)
    answer_2 = db.Column(db.Text(), nullable=True)
    answer_3 = db.Column(db.Text(), nullable=True)
    answer_4 = db.Column(db.Text(), nullable=True)
    correct_answer = db.Column(db.Integer, nullable=True)
    type_2_answer = db.Column(db.Boolean, nullable=True)
    correct_feedback = db.Column(db.Text(), nullable=False)
    incorrect_feedback = db.Column(db.Text(), nullable=False)


class surveyinput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    module_id = db.Column(db.Integer, db.ForeignKey("modules.id"))
    assessment_id = db.Column(db.Integer, db.ForeignKey("assessment_details.id"))
    question_1 = db.Column(db.Integer, nullable=False)
    question_2 = db.Column(db.Integer, nullable=False)
    question_3 = db.Column(db.Integer, nullable=False)
    question_4 = db.Column(db.Integer, nullable=False)
    question_5 = db.Column(db.Integer, nullable=False)
    question_6 = db.Column(db.Text, nullable=True)

    # passive_deletes=True


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))
