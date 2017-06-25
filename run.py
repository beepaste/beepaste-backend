from beepaste import app
from beepaste import web_cnf
from beepaste.utils.logger import lg


if __name__ == "__main__":
    lg(1, 'Starting server')
    app.run(**web_cnf)
