from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///primaryDatabase.db'
# app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
db = SQLAlchemy(app)

from AssessmentApp import routes

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

from flask_admin import Admin
from blog.views import AdminView
from blog.models import User, Post, Comment
admin = Admin(app,name='Admin panel', template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Comment, db.session))