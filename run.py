from beepaste import app
from beepaste import web_cnf
from beepaste.utils.logger import sendToLog


if __name__ == "__main__":
    sendToLog('INFO', 'starting beepaste api')
    app.run(**web_cnf)
