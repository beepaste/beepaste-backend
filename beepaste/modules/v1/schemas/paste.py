from marshmallow import Schema, fields, validate
import datetime
from beepaste.modules.v1.models.pasteFields import validEncriptions, validSyntax


class pasteSchema(Schema):
    author = fields.String(default="Anonymous",
                            validate=validate.Length(max=127, error="author name must be at most 127 chars long"))
    title = fields.String(default="Untitled",
                            validate=validate.Length(max=127, error="title must be at most 127 chars long"))

    expiryDate = fields.DateTime(default=datetime.datetime.utcnow())
    toExpire = fields.Boolean(default=False)

    raw = fields.String(required=True)
    encryption = fields.String(validate=validate.OneOf(choices=validEncriptions), default="no")
    syntax = fields.String(validate=validate.OneOf(choices=validSyntax), default="text")
