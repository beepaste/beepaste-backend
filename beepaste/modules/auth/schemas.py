from marshmallow import Schema, fields


class loginSchema(Schema):
    email = fields.Email(
            required=True,
            error_messages={'required': 'email is required.'}
            )
    password = fields.Str(
            required=True,
            error_messages={'required': 'password is required.'},
            load_only=True)
