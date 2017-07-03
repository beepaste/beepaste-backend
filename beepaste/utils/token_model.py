from SanicMongo import Document
from SanicMongo.fields import (StringField, IntField)

class TokenModel(Document):
    token = StringField(required=True, min_length=32, max_length=512)

    meta = {'collection': 'tokens'}

    async def getById(self, tokenid):
        curr_id = await self.objects(tokenid=tokenid).first()
        if curr_id is not None:
            ret_data_json = curr_id.to_json()
            ret_data = json.loads(ret_data_json)
            return ret_data
        else:
            return None
