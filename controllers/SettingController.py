from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *
import mysql.connector,sys,os

load_dotenv()
db = SQLAlchemy()
role_schema = RoleSchema2()
module_schema = ModulesSchema()
user_schema = UserSchema()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)


emptynavs = [6,7,8,9,10,11]
adminnavs = [1,2,3,4,5,12]

cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()



def role_index():
    if 'logged_in' in session:
        ###########################################
        checker = []
        for x in session['adminnav']:
            checker.append(x[0]['routeUri'])
            
        for x in session['emptynav']:
            checker.append(x[0]['routeUri'])
         ###########################################   
        if request.endpoint in checker:
            return render_template('role/index.html')
        else:
            return abort(403)
    else:
        return abort(401)



def role_show():
    roles = Role.query.all()
    data = role_schema.dump(roles,many=True)


    #AJAX
    output = ''
    ind = 0  
    for x in data:
        users_count = User.query.filter_by(role = x['id']).count()
        ind = ind + 1
        if ind % 2 == 0:
            trc = '<tr class="even">'
        else:
            trc = '<tr class="odd">'
        output = output + trc
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(ind)
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(x['group'])
        output = output + '<td class="dtr-control" tabindex="0" >{}</td>'.format(users_count)
        output = output + '<td>'
        output = output + '<button type="button" class="btn btn-success btn-xs" id="{}" onclick="editaccess(this)" ><i class="fa fa-object-ungroup"></i></button>'.format(x['id'])
        output = output + '<button type="button" class="btn btn-warning btn-xs" id="{}" onclick="useraccess(this)"><i class="fa fa-users-gear"></i></button>'.format(x['id'])
        output = output + '<button type="button" class="btn btn-info btn-xs" id="editro" data-group="{}" data-id="{}"><i class="fa fa-pencil"></i></button>'.format(x['group'],x['id'])
        output = output + '<button type="button" class="btn btn-danger btn-xs" id="delete" data-id="{}"><i class="fa fa-trash"></i></button>'.format(x['id'])
        output = output + '</td>'
        output = output + '</tr>' 
    return output
    
       

def role_store():
    data = request.get_json()
    cursor.execute("INSERT INTO `roles`(`group`, `log`, `modules`) VALUES (%s, %s, %s)",([data['rolename'],data['user'],","]))
    cnx.commit()
    return '1'

def role_update():
    data = request.get_json()
    cursor.execute("UPDATE `roles` SET `group`= %s WHERE `id` = %s",([data['rolename'],data['id']]))
    cnx.commit()
    return '1'

def role_destroy():
    data = request.get_json()
    cursor.execute("DELETE FROM `roles` WHERE  `id` = %s",([data['id']]))
    cursor.execute("UPDATE `users` SET `role`='0' WHERE `role` = %s",([data['id']]))
    cnx.commit()
    return  "1"




def mod_list(id):
    output=''
    access = Role.query.with_entities(Role.modules).filter(Role.id == id ).all()
    data = role_schema.dump(access,many=True) 
    str_arr = data[0]['modules'].split(",") # ['1', '2', '3']
    modules = Module.query.all()
    data_mode = module_schema.dump(modules,many=True) 
    for x in data_mode:
        if str(x['id']) in str_arr:
            output = output + '<div class="col-md-4"><input class="get_value" type="checkbox" name="modules[]" value="{}" checked><label for="modules">  {}</label></div>'.format(x['id'],x['module']) 

        else:
            output= output + '<div class="col-md-4"><input class="get_value" type="checkbox" name="modules[]" value="{}" ><label for="modules"> {}</label></div>'.format(x['id'],x['module']) 
    output= output + '<input type="hidden" name="type" value="{}" id="type">'.format(id)
    return output



def mod_update():
    data = request.get_json()
    cursor.execute("UPDATE `roles` SET `modules`=%s WHERE `id` = %s",([data['modules'],data['id']]))
    cnx.commit()
    role_user = Role.query.filter_by(id=int(session['role'])).first()
    ids = role_user.modules.split(",")
    desire_a = [int(id) for id in ids]
    shellempt = []
    shelladmin = []
    for id in desire_a:
        modules = Module.query.filter(Module.id == id ).all()
        data2 = module_schema.dump(modules,many=True)
        if id in adminnavs:
            shelladmin.append(data2)
        else:
            shellempt.append(data2)  
    session['adminnav'] = shelladmin
    session['emptynav'] = shellempt
    return  "1"

def userlist():
    users = User.query.filter(User.role != request.form.get('id')).all()
    data = user_schema.dump(users,many=True)
    output=''
    #output = output + '<select name="users" id="userss" style="width: 100%; color: green" multiple class = "select2bs4"> '
    for x in data:
        output = output + '<option  name="usersss[]"  value="{}">{}</option>'.format(x['id'],x['email'])
    #output = output + '</select>'
    output= output + '<input type="hidden" name="type" value="{}" id="type">'.format(request.form.get('id'))
    return output


def useraccessupdate():
    data = request.get_json()
    for x in data['upgru']:
        cursor.execute("UPDATE `users` SET `role`=%s WHERE `id` = %s",([data['id'],x]))
        cnx.commit()
    return '1'