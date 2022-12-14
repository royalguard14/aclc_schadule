from flask import Blueprint

'''
CONTROLLERS
'''
from controllers.AuthController import *
from controllers.CourseController import *
from controllers.DashboardController import *
from controllers.DepartmentController import *
from controllers.IpController import *
from controllers.ModuleController import *
from controllers.ProfileController import *
from controllers.ScheduleController import *
from controllers.SettingController import *
from controllers.SubjectController import *
from controllers.UserController import *
from controllers.AdminController import *
from controllers.RoomController import *

'''
Blueprints
'''
auth = Blueprint('auth', __name__) #
dashboards = Blueprint('dashboards', __name__)#
settings = Blueprint('settings', __name__) #
modules = Blueprint('modules', __name__) #
departments = Blueprint('departments', __name__)
courses = Blueprint('courses', __name__)
subjects = Blueprint('subjects', __name__)
schedules = Blueprint('schedules', __name__)
instructors = Blueprint('instructors', __name__)
students = Blueprint('students', __name__)
admins = Blueprint('admins', __name__)
users = Blueprint('users', __name__)
ipaccess = Blueprint('ipaccess', __name__)
rooms = Blueprint('rooms', __name__)

'''
ROUTES
'''

#Auth
auth.route('login',  methods=['GET','POST'])(login)
auth.route('/logout')(logout)

#Dashboard
dashboards.route('/')(dashboad_index)
dashboards.route('/d1')(dept_count)
dashboards.route('/d2')(course_count)
dashboards.route('/d3')(subj_count)
dashboards.route('/d4')(users_count)

#Setting/Role
settings.route('/', methods=['GET'])(role_index)
settings.route('/create', methods=['POST'])(role_store)
settings.route('/edit', methods=['POST'])(role_update)
settings.route('/delete', methods=['POST'])(role_destroy)
settings.route('modsList/<id>', methods=['POST','GET'])(mod_list)
settings.route('modsUpdate', methods = ['POST'])(mod_update)
settings.route('userlist', methods=['POST','GET'])(userlist)
settings.route('userupdate', methods=['POST','GET'])(useraccessupdate)
settings.route('/load_role')(role_show)




#Modules
modules.route('/', methods=['GET'])(module_index)
modules.route('/create', methods=['POST'])(module_store)
modules.route('/load_mod')(module_show)
modules.route('/edit', methods=['POST'])(module_update)
modules.route('/destroy', methods=['POST'])(module_destroy)
modules.route('/mod_icon', methods=['GET'])(module_icons)



#Department
departments.route('/', methods=['GET'])(dept_index)
departments.route('/create', methods=['POST','GET'])(dept_store)
departments.route('/edit', methods=['POST'])(dept_update)
departments.route('/delete', methods=['POST'])(dept_destroy)
departments.route('/show', methods=['GET'])(dept_show) 
departments.route('/edit_prog', methods=['POST'])(dept_update_progs)
departments.route('courseList/<id>', methods=['POST','GET'])(corse_list)
departments.route('corsUpdate', methods = ['POST'])(corse_update)



#Course
courses.route('/', methods=['GET'])(course_index)
courses.route('/create', methods=['POST'])(course_store)
courses.route('/edit', methods=['POST'])(course_update)
courses.route('/delete', methods=['POST'])(course_destroy)
courses.route('/show', methods=['GET'])(course_show)
courses.route('subjList/<id>', methods=['POST','GET'])(subj_list)
courses.route('subjUpdate', methods = ['POST'])(subjs_update)

#Subject
subjects.route('/', methods=['GET'])(subj_index)
subjects.route('/create', methods=['POST'])(subj_store)
subjects.route('/edit', methods=['POST'])(subj_update)
subjects.route('/delete', methods=['POST'])(subj_destroy)
subjects.route('/show', methods=['GET'])(subj_show)


#Schedule
schedules.route('/', methods=['GET'])(sched_index)
schedules.route('/create', methods=['POST'])(sched_store)
schedules.route('/edit', methods=['POST'])(sched_update)
schedules.route('/delete', methods=['POST'])(sched_destroy)

#Instructor
instructors.route('/', methods=['GET'])(instructor_index)
instructors.route('/create', methods=['POST'])(instructor_store)
instructors.route('/edit', methods=['POST'])(instructor_update)
instructors.route('/delete', methods=['POST'])(instructor_destroy)

#Student
students.route('/', methods=['GET'])(student_index)
students.route('/create', methods=['POST'])(student_store)
students.route('/edit', methods=['POST'])(student_update)
students.route('/delete', methods=['POST'])(student_destroy)

#
admins.route('/', methods=['GET'])(admin_index)
admins.route('/create', methods=['POST'])(admin_store)
admins.route('/edit', methods=['POST'])(admin_update)
admins.route('/delete', methods=['POST'])(admin_destroy)


#Rooms
rooms.route('/', methods=['GET'])(room_index)
rooms.route('/create', methods=['POST'])(room_store)
rooms.route('/edit', methods=['POST'])(room_update)
rooms.route('/delete', methods=['POST'])(room_destroy)
rooms.route('/show', methods=['GET'])(room_show)


#User
users.route('/', methods=['GET'])(user_index)
users.route('/create', methods=['POST'])(user_store)
users.route('/edit', methods=['POST'])(user_update)
users.route('/delete', methods=['POST'])(user_destroy)

#Ip Access
ipaccess.route('/', methods=['GET'])(ipa_index)
ipaccess.route('/create', methods=['POST'])(ipa_store)
ipaccess.route('/edit', methods=['POST'])(ipa_update)
ipaccess.route('/delete', methods=['POST'])(ipa_destroy)



