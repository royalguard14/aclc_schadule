from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from models.Models import *
from models.Schema import *
import sys

db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def ipa_index():
    ...

def ipa_store():
    ...

def ipa_show():
    ...

def ipa_update():
    ...

def ipa_destroy():
    ...