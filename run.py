from beepaste import app
from beepaste import web_cnf
from beepaste.utils.logger import lg


if __name__ == "__main__":
    app.run(**web_cnf)
