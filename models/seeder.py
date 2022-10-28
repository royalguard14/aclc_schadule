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
    Module(id= 1, module ='Import Files', description ='Import Department, Courses, Subject, Schedule and Student', routeUri ='admins.admin_index', icon ='fa-circle', default_url ='admin', encryptname ='434U8104D34600AC'),
    Module(id= 2, module ='Module', description ='Manage Modules', routeUri ='modules.module_index', icon ='fa-circle', default_url ='module', encryptname ='941O3670Y58216GE'),
    Module(id= 3, module ='Users', description ='Manage Users', routeUri ='users.user_index', icon ='fa-circle', default_url ='user', encryptname ='451I7747W54532BT'),
    Module(id= 4, module ='Ip Access', description ='Manage Ip Access', routeUri ='ipaccess.ipa_index', icon ='fa-circle', default_url ='ipa', encryptname ='860Z4360Z40888MB'),
    Module(id= 5, module ='Departments', description ='Manage Departments', routeUri ='departments.dept_index', icon ='fa-building', default_url ='department', encryptname ='243S5212V62259DO'),
    Module(id= 6, module ='Courses', description ='Manage Courses', routeUri ='courses.course_index', icon ='fa-folder-closed', default_url ='course', encryptname ='121W7965D83319ZE'),
    Module(id= 7, module ='Subjects', description ='Manage Subjects', routeUri ='subjects.subj_index', icon ='fa-lightbulb', default_url ='subject', encryptname ='261O3893J60604ZG'),
    Module(id= 8, module ='Schedules', description ='Manage Schedules', routeUri ='schedules.sched_index', icon ='fa-calendar-check', default_url ='schedule', encryptname ='485K4994Q49984KI'),
    Module(id= 9, module ='Instructors', description ='Manage Instructors', routeUri ='instructors.instructor_index', icon ='fa-chalkboard-user', default_url ='instructor', encryptname ='790Z4184C10740MS'),
    Module(id= 10, module ='Students', description ='Manage Students', routeUri ='students.student_index', icon ='fa-users-between-lines', default_url ='student', encryptname ='476Z7944T51754OQ'),
    Module(id= 11, module ='Setting', description ='Manage Setting', routeUri ='settings.role_index', icon ='fa-users-between-lines', default_url ='setting', encryptname ='476Z7944T51754OQsss'),
        
    ##Role
    Role(id= 1, group='Zear Developer', modules='1,2,3,4,5,6,7,8,9,10,11'),
    Role(id= 2, group='Administrator', modules='5,6,7,8,9,10'),
    Role(id= 3, group='Instructor', modules='7,10'),
    Role(id= 4, group='Student', modules='0'),
    
    ##Users
    User(email='zhie@caz.com', username='admin1', password=generate_password_hash('password', method='md5'), access='developer', online=1, active=1, role=1, link='wala' )
    User(email='chona@caz.com', username='admin2', password=generate_password_hash('password', method='md5'), access='admin', online=1, active=1, role=1, link='wala' )
    User(email='acog@caz.com', username='admin3', password=generate_password_hash('password', method='md5'), access='instructor', online=1, active=1, role=1, link='wala' )
]
  
db.bulk_save_objects(seeds)

db.commit()
db.close()
print("Successfully added a new post")