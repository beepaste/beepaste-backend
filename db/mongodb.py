import motor.motor_asyncio


class MongoDB(object):

    def __init__(self, config):
        assert type(config) == dict
        self.connString = 'mongodb://'
        if 'username' in config:
            self.connString += config['username'] + ':' + config['password'] + '@'
        self.connString += config['host'] + ':' + str(config['port']) + '/' + config['database']
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.connString)
        self.database = self.client[config['database']]

    async def insert(self, collection, document):
        result = self.database[collection].insert_one(document)
        return result
