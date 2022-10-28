from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv


nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
load_dotenv()
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
            cursor.execute('select id, dept_id, course_name, course_acronym from courses')
            data2 = cursor.fetchall()
            return render_template('course/index.html',course_list=data2)
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

def course_show():
    ...

def course_update():
    ...

def course_destroy():
    ...