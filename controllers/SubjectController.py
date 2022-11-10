from flask import render_template, redirect, url_for, request, abort, session,Response,json,jsonify
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *
subject_schema = SubjectSchema()

load_dotenv()
nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)

def subj_index():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'])
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'])
         ###########################################   
        if request.endpoint in checker:
            return render_template('subject/index.html')
        else:
            return abort(403)
    else:
        return abort(401)

def subj_store():
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
            units = str(data['lec_unit']) + "|" + str(data['lab_unit'])
            cursor.execute("INSERT INTO `subjects`(`subj_name`, `subj_code`, `units`, `pre_requisite`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s,%s)",([data['subject_name'],data['subject_code'], units, data['pre'],nows, nows]))
            cnx.commit()   
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def subj_show():
    subjects = Subject.query.all()
    data2 = subject_schema.dump(subjects,many=True) 
    #AJAX
    output = ''
    ind = 0      
    for x in data2:
        unitss = x['units'].split('|')
        sumunit = int(unitss[0]) + int(unitss[1])

        ind = ind + 1
        if ind % 2 == 0:
            trc = '<tr class="even">'
        else:
             trc = '<tr class="odd">'

        if x['pre_requisite'] == None:
            pr = 'No Data'
        else:
            pr = x['pre_requisite']

        output = output + trc
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(ind)
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['subj_name'])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['subj_code'])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(sumunit)
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(pr)
        output = output + '<td>'
        #output = output + '<button type="button" class="btn btn-success btn-xs" id="{}" onclick="editaccess(this)" ><i class="fa fa-folder-open"></i></button>'.format(x['id'])
        #output = output + '<button type="button" class="btn btn-warning btn-xs" id="edit_prog" data-id="{}" data-program="{}" ><i class="fa fa-graduation-cap"></i></button>'.format(x['id'], x['dept_program'])
        output = output + '<button type="button" class="btn btn-info btn-xs" id="edit"  data-id="{}" data-sname="{}" data-scode="{}" data-lac="{}" data-lab="{}" data-pre="{}" ><i class="fa fa-pencil"></i></button>'.format(x['id'], x['subj_name'], x['subj_code'], unitss[0], unitss[1], x['pre_requisite'])
        output = output + '<button type="button" class="btn btn-danger btn-xs" id="delete" data-id="{}"><i class="fa fa-trash"></i></button>'.format(x['id'])
        output = output + '</td>'
        output = output + '</tr>' 
    return output

def subj_update():
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
            units = str(data['lec_unit']) + "|" + str(data['lab_unit'])
            cursor.execute("UPDATE `subjects` SET `subj_name`= %s,`subj_code`= %s,`units`= %s,`pre_requisite`=%s,`updated_at`=%s WHERE `id` = %s",([data['subject_name'], data['subject_code'], units, data['pre'], nows, data['id']]))
            cnx.commit()   
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def subj_destroy():
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
                cursor.execute("DELETE FROM `subjects` WHERE `id`=%s ",([data['id']]))
                cnx.commit()
                return  "1"
            return abort(403)
        else:
            return abort(403)
    else:
        return abort(401)    
