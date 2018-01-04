from flask_sqlalchemy import SQLAlchemy, orm

db = SQLAlchemy()


# ---------------------data models---------------------


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = orm.relationship(Note, backref='user')


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = orm.relationship(Note, secondary='notes_tags', backref='tags')


# table for many-to-many relation between notes and tags
notes_tags = db.Table('notes_tags',
                      db.Model.metadata,
                      db.Column('note_id', db.Integer,
                                db.ForeignKey('note.id')),
                      db.Column('tag_id', db.Integer,
                                db.ForeignKey('tag.id'))
                      )
