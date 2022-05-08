from main import app

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///note_me.db'
db = SQLAlchemy(app)
