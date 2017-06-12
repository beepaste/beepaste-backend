from SanicMongo import connect
from beepaste import mongo_cnf
from beepaste import app


@app.listener('after_server_start')
async def notify_mongo_started(app, loop):
    # db init
    # TODO: write a logger to write logs to database!
    connect(**mongo_cnf)
