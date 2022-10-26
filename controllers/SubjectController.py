from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from models.Models import *
from models.Schema import *
import sys

db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def subj_index():
    ...

def subj_store():
    ...

def subj_show():
    ...

def subj_update():
    ...

def subj_destroy():
    ...