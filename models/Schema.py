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


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    link = fields.Str(required=True)

