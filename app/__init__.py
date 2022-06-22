""" Инициализация приложения, подключение и регистрация необходимых модулей. """

from flask import Flask
from flask_moment import Moment
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy

# REGISTRATION Block
app = Flask(__name__)
db = SQLAlchemy(app)
moment = Moment(app)
Markdown(app)

# CONFIGURATION Block
from .config import *

# Load modular scheme
from .model import *
from .view import *

if __name__ == '__main__':
    """ Использовать при первом запуске. Создает БД на основе моделей. """
    db.create_all()
