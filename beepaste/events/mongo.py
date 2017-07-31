from SanicMongo import connect
from beepaste import mongo_cnf
from beepaste import app
from beepaste.utils.logger import logg, get_logger, sendToLog, lg


@app.listener('after_server_start')
async def notify_mongo_started(app, loop):
    # db init
    # sendToLog('INFO', 'connecting to mongodb')
    await lg('INFO', 'connecting to mongodb')
    connect(**mongo_cnf)
