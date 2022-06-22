""" Файл конфигурации приложения """

import os, datetime
from dotenv import load_dotenv, find_dotenv
from . import app

load_dotenv(find_dotenv())

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = datetime.timedelta(days=float(os.environ.get("SESSION_LIFE")))
