import asyncio
import loop
import motor.motor_asyncio

class MongoDB(object):

    def __init__(self, config, collection):
        assert type(config) == dict
        self.connString = 'mongodb://'
        if 'username' in config:
            self.connString += config['username'] + ':' + config['password'] + '@'
        self.connString += config['host'] + ':' + config['port'] + '/' + config['database']
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.connString)
        self.database = self.client[ config['database'] ]
        self.collection = self.database[collection]

    def insert(self, document):
        result = self.collection.insert_one(document)
        return result
