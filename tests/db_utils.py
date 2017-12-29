"""Tools to manipulate and query database from model level"""
from pdb import set_trace as bp
from faker import Faker
from tireta.models import User, Note
from tireta import db
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
        print('{:^3} | {:^15}| {}'.format(note.id, note.user.name, note.name))


def add_user():
    user = User(name=fake.name())
    session.add(user)
    session.commit()
    return user


def add_note(author):
    note = Note(
        name=' '.join(fake.words()),
        body=fake.text(),
        user=author)
    session.add(note)
    session.commit()
    return note
