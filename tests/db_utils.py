"""Tools to manipulate and query database from model level"""
from pdb import set_trace as bp
from faker import Faker
from tireta.models import User, Note, Tag
from tireta import db
from sqlalchemy.orm.exc import NoResultFound
fake = Faker()
session = db.session


def clear_db():
    db.drop_all()
    db.create_all()


def list_users():
    print('---users---')
    for user in session.query(User):
        print('{:^3} | {:^15}'.format(user.id, user.name))


def list_notes():
    print('---notes---')
    for note in session.query(Note):
        print('{:^3} | {:^15}| {} | {}'.format(
            note.id,
            note.user.name,
            [tag.name for tag in note.tags], note.name))


def list_tags():
    print('---tags---')
    for tag in session.query(Tag):
        print('{:^3} | {:^15}'.format(tag.id, tag.name))


def list_db():
    list_users()
    list_notes()
    list_tags()


def add_user():
    """Add user to the database"""

    user = User(name=fake.name())
    session.add(user)
    session.commit()
    return user


def add_note(author):
    """Add note to the database

    The note belongs the the given user. Tags are also
     stored in the database and linked to the note.
    """
    tag_names = fake.words()
    tags = [add_tag(name) for name in tag_names]
    note = Note(
        name=' '.join(fake.words()),
        body=fake.text(),
        user=author,
        tags=tags)
    session.add(note)
    session.commit()
    return note


def add_tag(name):
    """Return tag object from db or add it if not present"""
    try:
        tag = session.query(Tag).filter_by(name=name).one()
    except(NoResultFound):
        tag = Tag(name=name)
        session.add(tag)
        session.commit
    return tag
