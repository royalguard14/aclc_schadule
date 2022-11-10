from marshmallow import fields, Schema

class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    group = fields.Str(required=True)
    modules = fields.Str(required=True)
    action = fields.Str(required=True)
    
class RoleSchema2(Schema):
    id = fields.Int(dump_only=True)
    group = fields.Str(required=True)
    modules = fields.Str(required=True)
    action = fields.Str(required=True)
    log = fields.Str(required=True)
    
class ModulesSchema(Schema):
    id = fields.Int(dump_only=True)
    module = fields.Str(required=True)
    description = fields.Str(required=True)
    routeUri = fields.Str(required=True)
    icon = fields.Str(required=True)
    default_url = fields.Str(required=True)
    encryptname = fields.Str(required=True)
#################################################

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    link = fields.Str(required=True)

class Depttab(Schema):
    id = fields.Int(dump_only=True)
    dept_name = fields.Str(required=True)

class Coursetab(Schema):
    id = fields.Int(dump_only=True)
    course_name = fields.Str(required=True)

class CourseAjax(Schema):
    id = fields.Int(dump_only=True)
    dept_id = fields.Int(dump_only=True)
    course_name = fields.Str(required=True)
    course_acronym = fields.Str(required=True)
################ALL####################
class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    dept_name = fields.Str(required=True)
    dept_acronym = fields.Str(required=True)
    dept_head = fields.Str(required=True)
    dept_course = fields.Str(required=True)
    dept_program = fields.Str(required=True)

class CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    dept_name = fields.Str(required=True)
    course_name = fields.Str(required=True)
    course_acronym = fields.Str(required=True)
    course_subject = fields.Str(required=True)

class SubjectSchema(Schema):
    id = fields.Int(dump_only=True)
    subj_name = fields.Str(required=True)
    subj_code = fields.Str(required=True)
    units = fields.Str(required=True)
    pre_requisite = fields.Str(required=True)

class RoomSchema(Schema):
    id = fields.Int(dump_only=True)
    room_name = fields.Str(required=True)
    room_type = fields.Str(required=True)
  

