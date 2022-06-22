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

# LOAD PACKAGES Block
from . import config
from . import model
from . import view

if __name__ == '__main__':
    """ Использовать при первом запуске. Создает БД на основе моделей. """
    model.db.create_all()
