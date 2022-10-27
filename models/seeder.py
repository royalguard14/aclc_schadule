from werkzeug.security import generate_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from Models import *
import os

load_dotenv()
DB_URL = "mysql+pymysql://{}:{}@localhost/{}".format(os.getenv("DB_USERNAME"),os.getenv("DB_PASSWORD"),os.getenv("DB_DATABASE"))
engine = create_engine(DB_URL)
local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
db = local_session()

seeds =[
    ##Module
    Module(module ='Import Files', description ='Import Department, Courses, Subject, Schedule and Student', routeUri ='admins.admin_index', icon ='fa-circle', default_url ='admin', encryptname ='434U8104D34600AC'),
    Module(module ='Module', description ='Manage Modules', routeUri ='modules.module_index', icon ='fa-circle', default_url ='module', encryptname ='941O3670Y58216GE'),
    Module(module ='Users', description ='Manage Users', routeUri ='users.user_index', icon ='fa-circle', default_url ='user', encryptname ='451I7747W54532BT'),
    Module(module ='Ip Access', description ='Manage Ip Access', routeUri ='ipaccess.ipa_index', icon ='fa-circle', default_url ='ipa', encryptname ='860Z4360Z40888MB'),
    Module(module ='Departments', description ='Manage Departments', routeUri ='departments.dept_index', icon ='fa-building', default_url ='department', encryptname ='243S5212V62259DO'),
    Module(module ='Courses', description ='Manage Courses', routeUri ='courses.course_index', icon ='fa-folder-closed', default_url ='course', encryptname ='121W7965D83319ZE'),
    Module(module ='Subjects', description ='Manage Subjects', routeUri ='subjects.subj_index', icon ='fa-lightbulb', default_url ='subject', encryptname ='261O3893J60604ZG'),
    Module(module ='Schedules', description ='Manage Schedules', routeUri ='schedules.sched_index', icon ='fa-calendar-check', default_url ='schedule', encryptname ='485K4994Q49984KI'),
    Module(module ='Instructors', description ='Manage Instructors', routeUri ='instructors.instructor_index', icon ='fa-chalkboard-user', default_url ='instructor', encryptname ='790Z4184C10740MS'),
    Module(module ='Students', description ='Manage Students', routeUri ='students.student_index', icon ='fa-users-between-lines', default_url ='student', encryptname ='476Z7944T51754OQ'),
    Module(module ='Setting', description ='Manage Setting', routeUri ='settings.role_index', icon ='fa-users-between-lines', default_url ='setting', encryptname ='476Z7944T51754OQsss'),
        
    ##Role
    Role(group='Zear Developer', modules='11'),
    Role(group='Administrator', modules='0'),
    Role(group='Instructor', modules='0'),
    Role(group='Student', modules='0'),
    

    ##Users
    User(email='zhie@caz.com', username='admin', password=generate_password_hash('password', method='md5'), access='developer', online=1, active=1, role=1, link='wala' )
    
]
  
db.bulk_save_objects(seeds)

db.commit()
db.close()
print("Successfully added a new post")