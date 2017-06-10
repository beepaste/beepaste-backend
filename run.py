from beepaste import app
from beepaste import web_cnf, mongo_cnf
from beepaste import logger
from SanicMongo import connect



async def notify_server_started():
    # db init
    logger.info('initiating connection to mongodb using config')
    connect(**mongo_cnf)
    logger.info('connected to mongodb')

if __name__ == "__main__":
    logger.info('Starting server')
    application = app()
    application.add_task(notify_server_started())
    application.run(**web_cnf)
