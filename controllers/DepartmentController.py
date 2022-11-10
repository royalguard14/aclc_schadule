from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *
nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
load_dotenv()
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()
department_schema = DepartmentSchema()
course_schema = CourseSchema()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)

def dept_index():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'])
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'])
         ###########################################   
        if request.endpoint in checker:
            return render_template('department/index.html')
        else:
            return abort(403)
    else:
        return abort(401)

def dept_store():
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
            cursor.execute("INSERT INTO `departments`(`dept_name`, `dept_acronym`, `dept_head`, `dept_course`, `dept_program`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s,%s,%s)",([data['department_name'], data['acronym'], data['dhead'],'0','0', nows, nows]))
            cnx.commit()
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def dept_show():
    departments = Department.query.all()
    data2 = department_schema.dump(departments,many=True) 
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
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['dept_name'])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['dept_acronym'])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['dept_head'])
        output = output + '<td>'
        output = output + '<button type="button" class="btn btn-success btn-xs" id="{}" onclick="editaccess(this)" ><i class="fa fa-folder-open"></i></button>'.format(x['id'])
        output = output + '<button type="button" class="btn btn-warning btn-xs" id="edit_prog" data-id="{}" data-program="{}" ><i class="fa fa-graduation-cap"></i></button>'.format(x['id'], x['dept_program'])
        output = output + '<button type="button" class="btn btn-info btn-xs" id="edit"  data-id="{}" data-deptname="{}" data-acrn="{}" data-head="{}" ><i class="fa fa-pencil"></i></button>'.format(x['id'], x['dept_name'], x['dept_acronym'], x['dept_head'])
        output = output + '<button type="button" class="btn btn-danger btn-xs" id="delete" data-id="{}"><i class="fa fa-trash"></i></button>'.format(x['id'])
        output = output + '</td>'
        output = output + '</tr>' 
    return output

def dept_update():
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
            cursor.execute("UPDATE `departments` SET `dept_name`= %s,`dept_acronym`=%s,`dept_head`=%s, `updated_at`=%s WHERE `id` = %s",([data['department_name'],data['acronym'],data['dhead'], nows, data['id']]))
            cnx.commit()
            return  "1"
        else:
            return abort(403)
    else:
        return abort(401)

def dept_update_progs():
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
            cursor.execute("UPDATE `departments` SET `dept_program`=%s , `updated_at`=%s  WHERE `id` =%s ",([data['prog'], nows, data['id']]))
            cnx.commit()
            return  "1"
        else:
            return abort(403)
    else:
        return abort(401)

def dept_destroy():
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
                cursor.execute("DELETE FROM `departments` WHERE `id`=%s ",([data['id']]))
                cnx.commit()
                return  "1"
            return abort(403)
        else:
            return abort(403)
    else:
        return abort(401)    

def corse_list(id):
    output=''
    access = Department.query.with_entities(Department.dept_course).filter(Department.id == id ).all()
    data = department_schema.dump(access,many=True) 
    str_arr = data[0]['dept_course'].split(",") # ['1', '2', '3']
    courses = Course.query.all()
    data_mode = course_schema.dump(courses,many=True) 
    for x in data_mode:
        if str(x['id']) in str_arr:
            output = output + '<div class="col-md-4"><input class="get_value" type="checkbox" name="modules[]" value="{}" checked><label for="modules">  {}</label></div>'.format(x['id'],x['course_name']) 
        else:
            output= output + '<div class="col-md-4"><input class="get_value" type="checkbox" name="modules[]" value="{}" ><label for="modules"> {}</label></div>'.format(x['id'],x['course_name']) 
    output= output + '<input type="hidden" name="type" value="{}" id="type">'.format(id)
    return output

def corse_update():
    data = request.get_json()
    cursor.execute("UPDATE `departments` SET `dept_course`=%s WHERE `id` = %s",([data['modules'],data['id']]))
    cnx.commit()
    return  "1"
