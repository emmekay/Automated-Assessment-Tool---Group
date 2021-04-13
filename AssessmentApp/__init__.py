from AssessmentApp import routes
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager # EK Added 


app = Flask(__name__)

app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///primaryDatabase.db'
# app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
# db = SQLAlchemy(app) # EK commeted out - was listed twice 

from AssessmentApp import routes # EK edited route input 

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# EK commented out - Shouldn't have blog references
#from blog import routes

#from flask_admin import Admin
#from blog.views import AdminView
#from blog.models import User, Post, Comment
#admin = Admin(app,name='Admin panel', template_mode='bootstrap3')
#admin.add_view(AdminView(User, db.session))
#admin.add_view(AdminView(Post, db.session))
#admin.add_view(AdminView(Comment, db.session))
