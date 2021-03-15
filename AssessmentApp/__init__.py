from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///primaryDatabase.db'
# app.config["SECRET_KEY"] = 'dqOTxaMwwDDEzBSk1PE_5zeJ_ow'
db = SQLAlchemy(app)

from AssessmentApp import routes
