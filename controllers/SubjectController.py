from flask import render_template, redirect, url_for, request, abort, session,Response,json,jsonify
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *


dept_schema = Depttab()
course_schema = Coursetab()
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
            dept = Department.query.all()
            data_s = dept_schema.dump(dept,many=True) 

            coursss = Course.query.all()
            data_s2 = course_schema.dump(coursss,many=True) 

            dept_dics = {}
            for ddd in data_s:
                ids = str(ddd['id'])
                vals = ddd['dept_name']
                dept_dics[ids] = vals

            corse_dics ={}
            for ddds in data_s2:
                ids2 = str(ddds['id'])
                vals2 = ddds['course_name']
                corse_dics[ids2] = vals2


            cursor.execute('SELECT `id`, `course_id`, `subj_name`, `subj_code`, `units`, `pre_requisite`, `syr` FROM `subjects`')
            data1 = cursor.fetchall()



            return render_template('subject/index.html',subj_list = data1,course_list=corse_dics,dept_list = dept_dics)
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
            syr = str(data['year']) + "|" + str(data['sem'])
            
            cursor.execute("INSERT INTO `subjects`(`course_id`, `subj_name`, `subj_code`, `units`, `pre_requisite`, `syr`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",([data['select_course'],data['subject_name'],data['subject_code'],units,data['pre'],syr,nows, nows]))
            cnx.commit()   
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def subj_show():
    ...

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
            syr = str(data['year']) + "|" + str(data['sem'])
            print('======>', data)
            cursor.execute("UPDATE `subjects` SET  `course_id`= %s, `subj_name`= %s, `subj_code`= %s, `units`= %s, `pre_requisite`= %s, `syr`= %s, `updated_at`= %s  WHERE `id` = %s",([data['select_course'], data['subject_name'], data['subject_code'], units, data['pre'], syr, nows, data['id']]))
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
                cursor.execute("DELETE FROM `schedules` WHERE `subj_id`=%s ",([data['id']]))
                cnx.commit()
                return  "1"
            return abort(403)
        else:
            return abort(403)
    else:
        return abort(401)    



def yearajax():
    data = [(0,'Select Year'),('1st','First Year'),('2nd','Second Year'),('3rd','Third Year'),('4th','Forth Year')]
    return data

def semajax():
    data = [(0,'Select Semester'),('1st','First Semester'),('2nd','Second Semester'),('3rd','Third Semester')]
    return data