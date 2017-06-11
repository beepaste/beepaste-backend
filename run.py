from beepaste import app
from beepaste import web_cnf
from beepaste import logger


if __name__ == "__main__":
    logger.info('Starting server')
    app.run(**web_cnf)
