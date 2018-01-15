from flask_sqlalchemy import SQLAlchemy, orm
from sqlalchemy.orm import relationship

db = SQLAlchemy()


# ---------------------data models---------------------


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = relationship('Note', back_populates='user')

    def __repr__(self):
        return 'User(id={},name=\'{}\',notes:{})'.format(self.id, self.name, [n.id for n in self.notes])


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='notes')
    tags = relationship(
        'Tag', secondary='notes_tags', back_populates='notes')

    def __repr__(self):
        return 'Note(id={},name=\'{}\',user_id={},tags={})'\
            .format(self.id,
                    self.name,
                    self.user_id,
                    ['{}({})'.format(tag.name, tag.id) for tag in self.tags])


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = relationship(
        'Note', secondary='notes_tags', back_populates='tags')

    def __repr__(self):
        return 'Tag(id={},name=\'{}\')'.format(self.id, self.name, [n.id for n in self.notes])

# table for many-to-many relation between notes and tags
notes_tags = db.Table('notes_tags',
                      db.Model.metadata,
                      db.Column('note_id', db.Integer,
                                db.ForeignKey('note.id')),
                      db.Column('tag_id', db.Integer,
                                db.ForeignKey('tag.id'))
                      )
