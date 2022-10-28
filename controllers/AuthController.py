from flask import render_template, redirect, url_for, request, abort, session,Response,json,Flask,flash
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *


db = SQLAlchemy()
load_dotenv()


emptynavs = [5,6,7,8,9,10]
adminnavs = [1,2,3,4,11]

role_schema = RoleSchema()
module_schema = ModulesSchema()
user_schema = UserSchema()



def login():
    if 'logged_in' in session:
        return redirect(url_for('dashboards.dashboad_index'))
    else:
        if request.method == 'POST':
            usernamePost = request.form.get('username')
            passwordPost = request.form.get('password')
            user = User.query.filter_by(username=usernamePost).first()
            if user:
                if check_password_hash(user.password, passwordPost):
                    session['logged_in'] = True
                    session['name'] = user.email
                    session['role'] = user.role
                    role_user = Role.query.filter_by(id=int(user.role)).first()
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
      
                    
                    return redirect(url_for('dashboards.dashboad_index'))
            
                else:
                    print('Incorrect Password')
            else:
                print('Username not available, Contact the Administrator')
              
    return render_template('auth/login.html')

def logout():
    session.clear()
    return redirect(url_for('auth.login'))

















