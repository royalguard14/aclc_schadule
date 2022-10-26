from flask import Flask, render_template
from flask_migrate import Migrate
from models.Models import db
from routes.web import auth,dashboards,settings,modules,departments,courses,subjects,schedules,instructors,students,admins,users,ipaccess

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(dashboards, url_prefix='/dashboard')
app.register_blueprint(settings, url_prefix='/setting')
app.register_blueprint(modules, url_prefix='/module')
app.register_blueprint(departments, url_prefix='/department')
app.register_blueprint(courses, url_prefix='/course')
app.register_blueprint(subjects, url_prefix='/subject')
app.register_blueprint(schedules, url_prefix='/schedule')
app.register_blueprint(instructors, url_prefix='/instructor')
app.register_blueprint(students, url_prefix='/student')
app.register_blueprint(admins, url_prefix='/admin')
app.register_blueprint(users, url_prefix='/user')
app.register_blueprint(ipaccess, url_prefix='/ip')



###################################################

@app.route('/')
def index():
    return '<h1> FrontPage </h1>'
#####################ERRORS########################

@app.errorhandler(401)
def error_401(e):
    code_no = '401'
    code_d = 'Unauthorized Access'
    return render_template('errors/main.html',code=code_no, desc = code_d)

@app.errorhandler(403)
def error_403(e):
    code_no = '403'
    code_d = 'Access Forbidden'
    return render_template('errors/main.html',code=code_no, desc = code_d)

@app.errorhandler(404)
def error_404(e):
    code_no = '404'
    code_d = 'Invalid Page'
    return render_template('errors/main.html',code=code_no, desc = code_d)

@app.errorhandler(500)
def error_500(e):
    code_no = '500'
    code_d = 'Server Error'
    return render_template('errors/main.html',code=code_no, desc = code_d)

@app.errorhandler(502)
def error_502(e):
    code_no = '502'
    code_d = 'Bad Gateway'
    return render_template('errors/main.html',code=code_no, desc = code_d)

@app.errorhandler(503)
def error_503(e):
    code_no = '503'
    code_d = 'Service Unavailable'
    return render_template('errors/main.html',code=code_no, desc = code_d)

@app.errorhandler(504)
def error_504(e):
    code_no = '504'
    code_d = 'Getway Timeout'
    return render_template('errors/main.html',code=code_no, desc = code_d)
####################################################


if __name__ == '__main__':
    app.debug = True
    app.run()


















