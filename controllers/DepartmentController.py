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
            cursor.execute('select id, dept_name, dept_acronym from departments')
            data2 = cursor.fetchall()
            return render_template('department/index.html',dept_list=data2)
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
            cursor.execute("INSERT INTO `departments`(`dept_name`, `dept_acronym`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s)",([data['department_name'],data['acronym'], nows, nows]))
            cnx.commit()
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)
      
def dept_show():
    cursor.execute('select id, dept_name, dept_acronym from departments')
    data2 = cursor.fetchall()
    
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
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x[1])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x[2])
        output = output + '<td><div class="btn-group"><a href="#" type="button" class="btn btn-outline-info btn-block btn-xs" id ="edit" data-id="{}" data-deptname="{}" data-acrn="{}"><i class="fa fa-pencil"></i> Edit</a></div>'.format(x[0], x[1],x[2])
        output = output + '<div class="btn-group"><a href="#" type="button" class="btn btn-outline-danger btn-block btn-xs"  id="delete" data-id="{}" ><i class="fa fa-trash"></i> delete</a></div></td>'.format(x[0])
        output = output + '</tr>' 
       
    
    return data2

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
            cursor.execute("UPDATE `departments` SET `dept_name`=%s,`dept_acronym`=%s,`updated_at`=%s WHERE `id` = %s",([data['department_name'],data['acronym'], nows,data['id']]))
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
    
    
    
    
    
    
