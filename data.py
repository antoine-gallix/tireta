import flask_sqlalchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey

db = flask_sqlalchemy.SQLAlchemy()


class Note(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    body = Column(Text)
