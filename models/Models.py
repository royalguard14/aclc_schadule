from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import DateTime
db = SQLAlchemy()
#===================================================
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(50))
    modules = db.Column(db.String(300))
    log = db.Column(db.String(100000))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'group': self.group,
            'modules': self.modules,
            'log': self.log,
        }
#===================================================
class Module(db.Model):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    module = db.Column(db.String(50))
    description = db.Column(db.String(1500))
    routeUri = db.Column(db.String(50))
    icon = db.Column(db.String(50))
    default_url = db.Column(db.String(50))
    encryptname = db.Column(db.String(500))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'module': self.module,
            'description': self.description,
            'routeUri': self.routeUri,
            'icon': self.icon,
            'default_url': self.default_url,
            'encryptname': self.encryptname
        }
#===================================================
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(25))
    password = db.Column(db.String(500))
    access = db.Column(db.String(120))
    online = db.Column(db.String(2))
    active = db.Column(db.String(2))
    role = db.Column(db.String(2))
    link = db.Column(db.String(500))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'access': self.access,
            'online': self.online,
            'active': self.active,
            'role': self.role,
            'link': self.link
        }
#===================================================   
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    firstaname = db.Column(db.String(20))
    middlename = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    suffix = db.Column(db.String(4))
    contact_no = db.Column(db.String(15))
    address = db.Column(db.String(150))
    bday = db.Column(db.DateTime)
    gender = db.Column(db.String(6))
    civil = db.Column(db.String(15))
    link = db.Column(db.String(500))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'firstaname': self.firstaname,
            'middlename': self.middlename,
            'lastname': self.lastname,
            'suffix': self.suffix,
            'contact_no': self.contact_no,
            'address': self.address,
            'bday': self.bday,
            'gender': self.gender,
            'civil': self.civil,
            'link': self.link
        }
#===================================================
class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(50))
    dept_acronym = db.Column(db.String(10))
    dept_head = db.Column(db.String(50))
    dept_course = db.Column(db.String(500))
    dept_program = db.Column(db.String(500))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'dept_name': self.dept_name,
            'dept_acronym': self.dept_acronym,
            'dept_head': self.dept_head,
            'dept_course': self.dept_course,
            'dept_program': self.dept_program
        }
#===================================================
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(25))
    course_acronym = db.Column(db.String(10))
    course_subject = db.Column(db.String(10))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'dept_id': self.dept_id,
            'course_name': self.course_name,
            'course_acronym': self.course_acronym,
            'course_subject': self.course_subject
        }
#===================================================
class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    subj_name = db.Column(db.String(50))
    subj_code = db.Column(db.String(10))
    units = db.Column(db.String(10))
    pre_requisite = db.Column(db.String(500))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'subj_name': self.subj_name,
            'subj_code': self.subj_code,
            'units': self.units,
            'pre_requisite': self.pre_requisite,
        }
#===================================================
class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(50))
    room_type = db.Column(db.String(10))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'room_name': self.room_name,
            'room_type': self.room_type,
        }
#===================================================
# class Schedule(db.Model):
#     __tablename__ = 'schedules'
#     id = db.Column(db.Integer, primary_key=True)
#     subj_id = db.Column(db.String(50))
#     sched_json = db.Column(db.String(5000))
#     created_at = db.Column(DateTime, default=datetime.now)
#     updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
#     @property
#     def serialize(self):
#         return {
#             'id': self.id,
#             'subj_id': self.subj_id,
#             'sched_json': self.sched_json,
#         }
#===================================================
# class SchoolR(db.Model):
#     __tablename__ = 'school_records'
#     id = db.Column(db.Integer, primary_key=True)
#     usn = db.Column(db.String(50))
#     accademic_year = db.Column(db.String(25))
#     course = db.Column(db.String(50))
#     year = db.Column(db.String(10))
#     study_load = db.Column(db.String(10000))
#     created_at = db.Column(DateTime, default=datetime.now)
#     updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
#     @property
#     def serialize(self):
#         return {
#             'id': self.id,
#             'usn': self.usn,
#             'accademic_year': self.accademic_year,
#             'course': self.course,
#             'year': self.year,
#             'study_load': self.study_load,
#         }
