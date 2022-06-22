""" Файл с описанием моделей приложения. """

from datetime import datetime

from . import db


class Creator(db.Model):
    __tablename__ = "creator"
    id_creator = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    pwd = db.Column(db.String(500), nullable=False)

    # Relationships
    # note = relationship('Note', back_populates='note', cascade="all, delete", passive_deletes=True)
    # profile = relationship('Profile', back_populates='profile', cascade="all, delete", passive_deletes=True, uselist=False)

    def __repr__(self):
        return f'<User {self.id_creator}>'


class Profile(db.Model):
    __tablename__ = "profile"
    id_profile = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('creator.id_creator', ondelete='CASCADE'), unique=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    first_name = db.Column(db.String(124), nullable=True)
    last_name = db.Column(db.String(126), nullable=True)
    bday = db.Column(db.DateTime, nullable=True)
    avatar = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f'<UserProfile №{self.id_profile} - {self.username}>'


class Note(db.Model):
    __tablename__ = "note"
    id_note = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(150), nullable=False)
    body = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, nullable=True)
    preview = db.Column(db.String(250), nullable=True)
    is_pinned = db.Column(db.Boolean, default=False)
    is_public = db.Column(db.Boolean, default=False)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('creator.id_creator', ondelete='CASCADE'))

    def __repr__(self):
        return '<Note %r>' % self.id_note


class Category(db.Model):
    __tablename__ = "category"
    id_category = db.Column(db.Integer, primary_key=True)
    notion = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Category %r>' % self.id_category
