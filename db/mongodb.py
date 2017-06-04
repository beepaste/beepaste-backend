import motor.motor_asyncio


class MongoDB(object):

    def __init__(self, config):
        assert type(config) == dict
        self.connString = f'mongodb://{config['username'}:config['password']@config['host']:str(config['port'])/config['database']'
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.connString)
        self.database = self.client[config['database']]

    def insert(self, collection, document):
        return self.database[collection].insert_one(document)

    def count(self, collection, query):
        return self.database[collection].find(query).count()
