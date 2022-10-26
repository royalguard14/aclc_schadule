from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *
import mysql.connector,os,ast,sys

db = SQLAlchemy()
load_dotenv()
module_schema = ModulesSchema()

cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)


def module_index():
    modules = Module.query.all()
    data = module_schema.dump(modules,many=True) 
    f = open("./static/fafontawsome.json", "r")
    fass = f.read()
    dictionary = ast.literal_eval(fass)
    
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'])
            
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'])
         ###########################################   
        if request.endpoint in checker:
            return render_template('module/index.html',modules = data,fawsome=dictionary)
        else:
            return abort(403)
    else:
        return abort(401)
    
            
def module_store():
    data = request.get_json()
    cursor.execute("INSERT INTO `modules`(`module`, `description`, `routeUri`, `icon`, `default_url`) VALUES (%s, %s, %s, %s, %s)",([data['module_name'],data['module_description'],data['module_url'],data['module_icon'],data['module_durl']]))
    cnx.commit()
    return  '1'

def module_show():
    modules = Module.query.all()
    data = module_schema.dump(modules,many=True) 
    return custom_response(data, 200)

def module_update():
    data = request.get_json()
    cursor.execute("UPDATE `modules` SET `module`= %s ,`description`= %s, `routeUri`= %s, `icon`= %s, `default_url`= %s  WHERE `id` = %s ",([data['module_name'],data['module_description'],data['module_url'],data['module_icon'],data['module_durl'],data['id']]))
    cnx.commit()
    return  '1'

def module_destroy():
    data = request.get_json()
    cursor.execute("DELETE FROM `modules` WHERE `id` = %s",([data['id']]))
    cnx.commit()
    return  '1'
