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


"""class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment_details.id'))
    question_1 = db.Column(db.Integer, nullable=False)
    question_2 = db.Column(db.Integer, nullable=False)
    question_3 = db.Column(db.Integer, nullable=False)
    question_4 = db.Column(db.Integer, nullable=False)
   # question_5 = db.Column(db.Integer, nullable=False)
    #question_6 = db.Column(db.Text, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)"""


from AssessmentApp import routes








# EK commented out below as "blog" shouldn't be used in our code
#from blog import routes

#from flask_admin import Admin
#from blog.views import AdminView
#from blog.models import User, Post, Comment
#admin = Admin(app,name='Admin panel', template_mode='bootstrap3')
#admin.add_view(AdminView(User, db.session))
#admin.add_view(AdminView(Post, db.session))
#admin.add_view(AdminView(Comment, db.session))
