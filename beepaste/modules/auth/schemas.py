from marshmallow import Schema, fields


class loginSchema(Schema):
    username = fields.Str(
            required=True,
            error_messages={'required': 'username is required.'}
            )
    password = fields.Str(
            required=True,
            error_messages={'required': 'password is required.'},
            load_only=True)
