from flask import render_template, redirect, url_for, request, abort, session,Response,json,jsonify
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *
dept_schema = Depttab()
course_schema = CourseSchema()
subject_schema = SubjectSchema()
load_dotenv()
nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)

def course_index():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'])
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'])
         ###########################################   
        if request.endpoint in checker:
            return render_template('course/index.html')
        else:
            return abort(403)
    else:
        return abort(401)

def course_store():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'].split(".")[0])
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'].split(".")[0])
         ###########################################   
        if request.endpoint.split(".")[0] in checker:
            data = request.get_json()
            cursor.execute("INSERT INTO `courses`(`course_name`, `course_acronym`, `course_subject`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s)",([data['course_name'], data['course_code'], '0', nows, nows]))
            cnx.commit()
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def course_show(): #for ajax
    courses = Course.query.all()
    data2 = course_schema.dump(courses,many=True) 
    #AJAX
    output = ''
    ind = 0      
    for x in data2:
        ind = ind + 1
        if ind % 2 == 0:
            trc = '<tr class="even">'
        else:
             trc = '<tr class="odd">'
        output = output + trc
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(ind)
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['course_name'])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['course_acronym'])
        output = output + '<td>'
        output = output + '<button type="button" class="btn btn-success btn-xs" id="{}" onclick="editaccess(this)" ><i class="fa fa-lightbulb"></i></button>'.format(x['id'])
        output = output + '<button type="button" class="btn btn-info btn-xs" id="edit"  data-id="{}" data-corsname="{}" data-acrn="{}"  ><i class="fa fa-pencil"></i></button>'.format(x['id'], x['course_name'], x['course_acronym'],)
        output = output + '<button type="button" class="btn btn-danger btn-xs" id="delete" data-id="{}"><i class="fa fa-trash"></i></button>'.format(x['id'])
        output = output + '</td>'
        output = output + '</tr>' 
    return output

def course_update():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'].split(".")[0])
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'].split(".")[0])
         ###########################################   
        if request.endpoint.split(".")[0] in checker:
            data = request.get_json()
            cursor.execute("UPDATE `courses` SET `course_name`=%s,`course_acronym`=%s,`updated_at`=%s WHERE `id` = %s",([data['course_name'], data['course_code'], nows, data['id']]))
            cnx.commit()
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def course_destroy():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'].split(".")[0])
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'].split(".")[0])
         ###########################################   
        if request.endpoint.split(".")[0] in checker:
            if session['role'] == '1' or  session['role'] == '2':
                data = request.get_json()
                cursor.execute("DELETE FROM `courses` WHERE `id`=%s ",([data['id']]))
                cnx.commit()
                return  "1"
            return abort(403)
        else:
            return abort(403)
    else:
        return abort(401)    


def subj_list(id):
    output=''
    access = Course.query.with_entities(Course.course_subject).filter(Course.id == id ).all()
    data = course_schema.dump(access,many=True) 
    str_arr = data[0]['course_subject'].split(",") # ['1', '2', '3']
    subjects = Subject.query.all()
    data_mode = subject_schema.dump(subjects,many=True) 
    
    for x in data_mode:
        if str(x['id']) in str_arr:
            output = output + '<div class="col-md-12">'
            output = output + '<input class="get_value" type="checkbox" name="modules[]" value="{}" checked><label for="modules">{}</label>'.format(x['id'],x['subj_name']) 
            output = output + '</div>'
        else:
            output = output + '<div class="col-md-12">'
            output = output + '<input class="get_value" type="checkbox" name="modules[]" value="{}" ><label for="modules"> {}</label>'.format(x['id'],x['subj_name']) 
            output = output + '</div>'
    output= output + '<input type="hidden" name="type" value="{}" id="type">'.format(id)


    return output


def subjs_update():
    data = request.get_json()
    cursor.execute("UPDATE `courses` SET `course_subject`=%s WHERE `id` = %s",([data['modules'],data['id']]))
    cnx.commit()
    return "1"