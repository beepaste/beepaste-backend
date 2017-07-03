from SanicMongo import connect
from beepaste import mongo_cnf
from beepaste import app
from beepaste.utils.logger import lg


@app.listener('after_server_start')
async def notify_mongo_started(app, loop):
    # db init
    await lg(1, 'connected to mongo')
    connect(**mongo_cnf)
