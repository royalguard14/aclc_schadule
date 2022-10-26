from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from models.Models import *
from models.Schema import *
import sys

db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)

##########
def instructor_index():
    ...

def instructor_store():
    ...

def instructor_show():
    ...

def instructor_update():
    ...

def instructor_destroy():
    ...
    
##########    
def student_index():
    ...

def student_store():
    ...

def student_show():
    ...

def student_update():
    ...

def student_destroy():
    ...