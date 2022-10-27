from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from models.Models import *
from models.Schema import *
import sys

db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def admin_index():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'])
            
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'])
         ###########################################   
        if request.endpoint in checker:
            return render_template('import/index.html')
        else:
            return abort(403)
    else:
        return abort(401)

def admin_store():
    ...

def admin_show():
    ...

def admin_update():
    ...

def admin_destroy():
    ...
#################################
def import_dept():
    return 'upload department'
    
def import_cors():
    return 'upload course'

def import_subj():
    return 'upload subject'
    
def import_sched():
    return 'upload schedule'
    
def import_student():
    return 'upload student'
    
def import_inst():
    return 'upload instructor'
    
