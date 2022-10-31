from flask import render_template, redirect, url_for, request, abort, session,Response,json,jsonify
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import Department,Course
from models.Schema import Depttab

dept_schema = Depttab()
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
            dept = Department.query.all()
            data_s = dept_schema.dump(dept,many=True) 
            dics = {}
            for ddd in data_s:
                ids = str(ddd['id'])
                vals = ddd['dept_name']
                dics[ids] = vals
            cursor.execute('SELECT `id`, `dept_id`, `course_name`, `course_acronym` FROM `courses`')
            data2 = cursor.fetchall()
            return render_template('course/index.html',course_list=data2,dept_list = dics)
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
            cursor.execute("INSERT INTO `courses`(`dept_id`, `course_name`, `course_acronym`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s)",([data['dept_id'], data['course_name'], data['course_code'], nows, nows]))
            cnx.commit()
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def course_show(): #for ajax
    cursor.execute('SELECT `id`, `dept_id`, `course_name`, `course_acronym` FROM `courses`')
    data2 = cursor.fetchall()
    dept = Department.query.all()
    data_s = dept_schema.dump(dept,many=True) 
    dics = {}
    for ddd in data_s:
        ids = str(ddd['id'])
        vals = ddd['dept_name']
        dics[ids] = vals
    new_line=[]
    for x in data2:
        dic={}
        dic["no"] = len(new_line) + 1
        dic["id"] = x[0]
        dic["dept_id"] = dics[x[1]]
        dic["course_name"] = x[2]
        dic["course_acronym"] = x[3]
        new_line.append(dic)
    return new_line

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
            cursor.execute("UPDATE `courses` SET `dept_id`=%s,`course_name`=%s,`course_acronym`=%s WHERE `id` = %s",([data['dept'], data['subj'], data['code'], data['id']]))
            cnx.commit()
            return  "1"
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
                cursor.execute("DELETE FROM `subjects` WHERE `course_id`=%s ",([data['id']]))
                #NOTE: Delete schedule where subj_id = ?
                cnx.commit()
                return  "1"
            return abort(403)
        else:
            return abort(403)
    else:
        return abort(401)    


def for_subselect():
    cursor.execute('select id, course_name, course_acronym from courses')
    data2 = cursor.fetchall()
    return data2

