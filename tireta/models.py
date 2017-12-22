from sqlalchemy import Column, Integer, String, Text, ForeignKey
from flask_sqlalchemy import orm
from tireta import db


class Note(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    notes = orm.relationship(Note, backref='user')
