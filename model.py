from main import app

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///note_me.db'
db = SQLAlchemy(app)


class Note(db.Model):
    id_note = db.Column(db.Integer, primary_key=True)
    n_title = db.Column(db.String(150), nullable=False)
    n_pinned = db.Column(db.Boolean, default=False)
    n_tag = db.Column(db.String(150), nullable=False)
    n_body = db.Column(db.Text, nullable=True)
    n_date_c = db.Column(db.DateTime, default=datetime.utcnow)
    n_date_m = db.Column(db.DateTime, default=datetime.utcnow)
    n_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Note %r>' % self.id
