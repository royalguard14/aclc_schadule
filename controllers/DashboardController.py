from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from models.Models import *
from models.Schema import *
import sys

db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)

def dashboad_index():
    if 'logged_in' in session:
        return render_template('dashboard/index.html')
    else:
        return abort(401)
     
def dept_count():
    data = Department.query.count()
    return custom_response(data, 200)

def subj_count():
    data = Subject.query.count()
    return custom_response(data, 200)

def course_count():
    data = Course.query.count()
    return custom_response(data, 200)
    
def users_count():
    data = User.query.count()
    return custom_response(data, 200)
    
def student_count():
    ...

def instructor_count():
    ...
    
