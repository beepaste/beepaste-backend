from marshmallow import Schema, fields, validate, pre_load
import datetime
from beepaste.modules.v1.models.pasteFields import validEncriptions, validSyntax


class pasteSchema(Schema):
    author = fields.String(default="Anonymous",
                            validate=validate.Length(max=127, error="author name must be at most 127 chars long"))
    title = fields.String(default="Untitled",
                            validate=validate.Length(max=127, error="title must be at most 127 chars long"))

    uri = fields.String(required=True, dump_only=True,
                            validate=validate.Length(equal=6, error="uri must be exactly 6 chars long"))
    shorturl = fields.String(dump_only=True)

    expiryDate = fields.DateTime(default=datetime.datetime.utcnow(), load_only=True)
    expireAfter = fields.Integer(default=0, load_only=True)
    toExpire = fields.Boolean(default=False, load_only=True)

    raw = fields.String(required=True)
    encryption = fields.String(validate=validate.OneOf(choices=validEncriptions), default="no")
    syntax = fields.String(validate=validate.OneOf(choices=validSyntax), default="text")

    @pre_load
    def generate_expiryDate(self, in_data):
        if 'expireAfter' in in_data and in_data['expireAfter'] is not 0:
            in_data['expiryDate'] = (datetime.datetime.utcnow() + datetime.timedelta(seconds=int(in_data['expireAfter']))).isoformat()
            in_data['toExpire'] = True
