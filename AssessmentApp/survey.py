from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

#from AssessmentApp import app
#from AssessmentApp.models import *
import pymysql
import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.dates as mdates 

# open database 
#db = pymysql.connect("mysql+pymysql", "c2101138", "Password123", "csmysql.cs.cf.ac.uk:3306/c2101138_cmt313")
########

#prepare cursor() method 
cursor = db.cursor()

# SQL query to READ a record 
sql = "SELECT * FROM surveyinput \ WHERE id > {0}".format(0)

# execute SQL query using execute 
cursor.execute(sql)

# Fetch all rows in a list of lists. 
results = cursor.fetchall()
for row in results:
    id = row[0]
    q1 = row[1]
    q2 = row[2]
    q3 = row[3]
    q4 = row[4]
    q5 = row[5]
    q6 = row[6]

    # print fetched result
    print("id = {0}, q1 = {1}, q2 = {2}, q3 = {3}, q4 = {4}, q5 = {5}, q6 = {6}".format(id,q1,q2,q3,q4,q5,q6))


# disconnect from server 
db.close()

