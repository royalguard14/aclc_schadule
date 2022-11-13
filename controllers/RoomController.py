from flask import render_template, redirect, url_for, request, abort, session,Response,json,jsonify
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *


load_dotenv()
nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()


room_schema = RoomSchema()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def room_index():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'])
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'])
         ###########################################   
        if request.endpoint in checker:
            return render_template('room/index.html')
        else:
            return abort(403)
    else:
        return abort(401)
    

def room_store():
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
            cursor.execute("INSERT INTO `rooms`(`room_name`, `room_type`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s)",([data['room_name'],data['room_type'],nows, nows]))
            cnx.commit()   
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def room_show():
    rooms = Room.query.all()
    data2 = room_schema.dump(rooms,many=True) 
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
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['room_name'])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['room_type'])
        output = output + '<td>'
        output = output + '<button type="button" class="btn btn-info btn-xs" id="edit"  data-id="{}" data-rname="{}" data-rtype="{}"><i class="fa fa-pencil"></i></button>'.format(x['id'], x['room_name'], x['room_type'])
        output = output + '<button type="button" class="btn btn-danger btn-xs" id="delete" data-id="{}"><i class="fa fa-trash"></i></button>'.format(x['id'])
        output = output + '</td>'
        output = output + '</tr>' 
    return output

def room_update():
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
            cursor.execute("UPDATE `rooms` SET `room_name`=%s,`room_type`=%s,`updated_at`=%s WHERE `id` = %s",([data['room_name'], data['room_type'], nows, data['id']]))
            cnx.commit()   
            return '1'
        else:
            return abort(403)
    else:
        return abort(401)

def room_destroy():
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
                cursor.execute("DELETE FROM `rooms` WHERE `id`=%s ",([data['id']]))
                cnx.commit()
                return  "1"
            return abort(403)
        else:
            return abort(403)
    else:
        return abort(401)    