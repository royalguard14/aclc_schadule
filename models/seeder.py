from werkzeug.security import generate_password_hash
from datetime import date, datetime, timedelta
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
nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
wala = None



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
    Module(id= 9, module ='Rooms', description ='Manage Rooms', routeUri ='rooms.room_index', icon ='fa-calendar-check', default_url ='schedule', encryptname ='485K4994222Q49984KI'),
    Module(id= 10, module ='Instructors', description ='Manage Instructors', routeUri ='instructors.instructor_index', icon ='fa-chalkboard-user', default_url ='instructor', encryptname ='790Z4184C10740MS'),
    Module(id= 11, module ='Students', description ='Manage Students', routeUri ='students.student_index', icon ='fa-users-between-lines', default_url ='student', encryptname ='476Z7944T51754OQ'),
    Module(id= 12, module ='Setting', description ='Manage Setting', routeUri ='settings.role_index', icon ='fa-users-between-lines', default_url ='setting', encryptname ='476Z7944T51754OQsss'),
        
    ##Role
    Role(id= 1, group='Zear Developer', modules='1,2,3,4,5,6,7,8,9,10,11,12'),
    Role(id= 2, group='Administrator', modules='5,6,7,8,9,10,11'),
    Role(id= 3, group='Instructor', modules='7,11'),
    Role(id= 4, group='Student', modules='0'),
    
    ##Users
    User(email='zhie@caz.com', username='admin', password=generate_password_hash('password', method='md5'), access='developer', online=1, active=1, role=1, link='wala' ),
    User(email='chona@caz.com', username='admin1', password=generate_password_hash('password', method='md5'), access='admin', online=1, active=1, role=2, link='wala' ),
    User(email='acog@caz.com', username='admin2', password=generate_password_hash('password', method='md5'), access='instructor', online=1, active=1, role=3, link='wala' ),
    User(email='cha@caz.com', username='admin3', password=generate_password_hash('password', method='md5'), access='instructor', online=1, active=1, role=4, link='wala' ),

    #ACLC BUTUAN DATA Department


    Department( id = 1 , dept_name = 'Computer Education Department', dept_acronym = 'CED', dept_head = 'Junell Bojocan', dept_course = '0', dept_program = 'BSIT,BSCS', created_at = nows, updated_at = nows),
 


    #ACLC BUTUAN DATA Courses 
    Course(id = 1, course_name = 'AI Course', course_acronym = 'AI', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 2, course_name = 'BED Course', course_acronym = 'BED', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 3, course_name = 'COMP Course', course_acronym = 'COMP', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 4, course_name = 'CPMJ Course', course_acronym = 'CPMJ', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 5, course_name = 'CS Course', course_acronym = 'CS', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 6, course_name = 'ENGL Course', course_acronym = 'ENGL', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 7, course_name = 'ETHNS Course', course_acronym = 'ETHNS', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 8, course_name = 'FILI Course', course_acronym = 'FILI', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 9, course_name = 'GE Course', course_acronym = 'GE', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 10, course_name = 'IS Course', course_acronym = 'IS', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 11, course_name = 'IT Course', course_acronym = 'IT', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 12, course_name = 'ITE Course', course_acronym = 'ITE', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 13, course_name = 'MATH Course', course_acronym = 'MATH', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 14, course_name = 'NSCI Course', course_acronym = 'NSCI', course_subject = '0', created_at = nows , updated_at = nows),
    Course(id = 15, course_name = 'PHYED Course', course_acronym = 'PHYED', course_subject = '0', created_at = nows , updated_at = nows),


    #ACLC BUTUAN DATA Courses 
    Subject(id = 1 , subj_name='Application Development and Emerging Technology' , subj_code = '6200' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 2 , subj_name='Application Life Cycle Management' , subj_code = '6302' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 3 , subj_name='Architecture and Organization' , subj_code = '6204' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 4 , subj_name='Automata Theory and Formal Language' , subj_code = '6205' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 5 , subj_name='Business Software Packages' , subj_code = 'BSP' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 6 , subj_name='Calculus 1' , subj_code = '6100' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 7 , subj_name='Calculus-Based Physics 1' , subj_code = '6100' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 8 , subj_name='Calculus-Based Physics 2' , subj_code = '6101' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 9 , subj_name='Capstone Project' , subj_code = '600' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 10 , subj_name='Cloud Computing and the Internet of Things' , subj_code = '6300' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 11 , subj_name='Computer Programming 1' , subj_code = '6102' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 12 , subj_name='Computer Programming 2' , subj_code = '6104' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 13 , subj_name='Computing Fundamentals' , subj_code = '6101' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 14 , subj_name='CS Design Project 2' , subj_code = '6399' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 15 , subj_name='CS Major Elective 1 (Introduction to Robotics)' , subj_code = '6312' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 16 , subj_name='CS Major Elective 2 (Intelligent Systems - Machine Learning)' , subj_code = '6312A' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 17 , subj_name='CS Major Elective 4 (Game Engine Programming 2)' , subj_code = '6320' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 18 , subj_name='Current Trends and Issues in Information Systems' , subj_code = 'CTIIS' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 19 , subj_name='Current Trends in IT / Current Trends and Issues' , subj_code = '303 / 6013' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 20 , subj_name='Data Analysis' , subj_code = '6200' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 21 , subj_name='Data Communications and Networking 1' , subj_code = '6201' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 22 , subj_name='Data Communications and Networking 3' , subj_code = '6224' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 23 , subj_name='Data Communications and Networking 4' , subj_code = '6300' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 24 , subj_name='Data Structures and Algorithm' , subj_code = '6201' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 25 , subj_name='Database Management System 2' , subj_code = '402' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 26 , subj_name='Database Management Systems 1' , subj_code = '6202' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 27 , subj_name='Discrete Mathematics' , subj_code = '6105' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 28 , subj_name='Discrete Structures 2' , subj_code = '6201' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 29 , subj_name='Information Assurance and Security 1' , subj_code = '6205A' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 30 , subj_name='Information Assurance and Security 2' , subj_code = '6206A' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 31 , subj_name='Information Management' , subj_code = '6220' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 32 , subj_name='Integrative Programming and Technology 1' , subj_code = '6302' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 33 , subj_name='Introduction to Human Computer Interaction' , subj_code = '6200' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 34 , subj_name='Introduction to Multimedia' , subj_code = '6209' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 35 , subj_name='Introduction to Software Engineering' , subj_code = '409' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 36 , subj_name='IT Capstone Project 1' , subj_code = '6398' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 37 , subj_name='IT Free Elective (WST)' , subj_code = '6303' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 38 , subj_name='IT Major Elective 1' , subj_code = '6314' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 39 , subj_name='IT Major Elective 1 (OOP)' , subj_code = 'ELEC01' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 40 , subj_name='IT Major Elective 1 (WAD)' , subj_code = '6314' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 41 , subj_name='IT Major Elective 2 (Web Application Development 2)' , subj_code = '6315' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 42 , subj_name='IT Major Elective 3 (Mobile Applications Design and Development 1)' , subj_code = '6323A' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 43 , subj_name='IT Major Elective 4 (MADD2)' , subj_code = '6324A' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 44 , subj_name='IT Practicum' , subj_code = '6397' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 45 , subj_name='Load Testing' , subj_code = '6303' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 46 , subj_name='Modeling and Simulation' , subj_code = '6304' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 47 , subj_name='Multimedia Systems' , subj_code = '302' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 48 , subj_name='Network Security' , subj_code = '207' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 49 , subj_name='Principles of Operating Systems and its Application' , subj_code = '6206' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 50 , subj_name='Programming Language with Compiler' , subj_code = '6207' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 51 , subj_name='Project Management and Quality Systems' , subj_code = '202' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 52 , subj_name='Social and Professional Issues' , subj_code = '6202' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 53 , subj_name='Software Engineering 1' , subj_code = '6209' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 54 , subj_name='Software Engineering 2' , subj_code = '6300' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 55 , subj_name='System Administration and Maintenance' , subj_code = '6301' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 56 , subj_name='System Analysis and Design' , subj_code = '202' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 57 , subj_name='System Integration and Architecture 1' , subj_code = '6208' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 58 , subj_name='Technopreneurship' , subj_code = '6301' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 59 , subj_name='Unified Functional Testing' , subj_code = '6306' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 60 , subj_name='Web Design' , subj_code = 'WEB' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 61 , subj_name='Web Programming and Development' , subj_code = '410' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 62 , subj_name='Art Appreciation' , subj_code = '6115' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 63 , subj_name='Ethics' , subj_code = '6107' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 64 , subj_name='Euthenics 2' , subj_code = '6102' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 65 , subj_name='Life and Works of Jose Rizal' , subj_code = '6300' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 66 , subj_name='Mathematics in the Modern World' , subj_code = '6114' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 67 , subj_name='Pagsasaling Pampanitikan' , subj_code = '6301' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 68 , subj_name='Purposive Communication 2' , subj_code = '6100' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 69 , subj_name='Rhythmic Activities' , subj_code = '6102' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 70 , subj_name='Science Technology and Society' , subj_code = '6116' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 71 , subj_name='Team Sports' , subj_code = '6200' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 72 , subj_name='The Contemporary World' , subj_code = '6102' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 73 , subj_name='Wika Lipunan at Kultura' , subj_code = '6101' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 74 , subj_name='Individual/Dual Sports' , subj_code = '6103' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 75 , subj_name='Environmental Science' , subj_code = '6200' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 76 , subj_name='Understanding the Self' , subj_code = '6100' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 77 , subj_name='Kritikal na Pagbasa, Pagsulat at Pagsasalita' , subj_code = '6201' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 78 , subj_name='General Chemistry' , subj_code = '101' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 79 , subj_name='Purposive Communication 1' , subj_code = '6106' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 80 , subj_name='Technical Scientific and Business English' , subj_code = '6301' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 81 , subj_name='Physical Fitness' , subj_code = '6101' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 82 , subj_name='Readings in Philippine History' , subj_code = '6101' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
    Subject(id = 83 , subj_name='Pagbasa at Pagsulat Tungo sa Pananaliksik' , subj_code = '6200' , units = '0|0', pre_requisite = wala , created_at = nows, updated_at = nows),
]
  
db.bulk_save_objects(seeds)

db.commit()
db.close()
print("Successfully added a new post")