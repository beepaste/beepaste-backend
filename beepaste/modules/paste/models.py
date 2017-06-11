import datetime
from SanicMongo import Document
from SanicMongo.fields import (IntField, DateTimeField, StringField, URLField,
                               BooleanField)
import json
from pyshorteners import Shortener
from beepaste.utils.config import get_config
import string
from random import choice
from .field import validEncriptions, validSyntax



class PasteModel(Document):
    """
        The PASTE class have attributes for a paste such as
        raw text (encoded inBase64),
        pasteDate and expiretDate and so on! This class is developing.
    """

    author = StringField(default="Anonymous", max_length=127)
    title = StringField(default="Untitled", max_length=127)
    shorturl = URLField(default="https://beepaste.io/")
    uri = StringField(required=True, min_length=6, max_length=6)

    date = DateTimeField(default=datetime.datetime.utcnow())
    expiryDate = DateTimeField(default=datetime.datetime.utcnow())
    toExpire = BooleanField(default=False)

    raw = StringField(required=True)
    encryption = StringField(choices=validEncriptions, default="no")
    syntax = StringField(choices=validSyntax, default="text")

    views = IntField(default=0)
    ownerID = IntField(default=0)

    meta = {'collection': 'pastes'}

    def generate_uri(self, len=6):
        allchar = string.ascii_letters + string.digits
        return "".join(choice(allchar) for x in range(len))

    async def generate_url(self):
        new_uri = self.generate_uri()
        count = await Paste.objects(uri=new_uri).count()
        while count > 0:
            new_uri = self.generate_uri()
            count = await Paste.objects(uri=new_uri).count()

        self.uri = new_uri
        # access_token = get_config('bitly')['token']
        # shortener = Shortener('Bitly', bitly_token=access_token)
        # self.shorturl = shortener.short(url)
