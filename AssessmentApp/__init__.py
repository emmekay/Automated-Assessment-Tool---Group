from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///primaryDatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2101138:Password123@csmysql.cs.cf.ac.uk:3306/c2101138_cmt313'

# app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(user_id):
#     return user.query.get(int(user_id))


from AssessmentApp import routes




