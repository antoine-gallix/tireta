from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
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


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    notes = orm.relationship(Note, secondary='notes_tags', backref='tags')

notes_tags = Table('notes_tags',
                   db.Model.metadata,
                   Column('note_id', Integer, ForeignKey('note.id')),
                   Column('tag_id', Integer, ForeignKey('tag.id'))
                   )
