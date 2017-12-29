from pdb import set_trace as bp
from faker import Faker
from tireta.models import User
from tireta import db
fake = Faker()
session = db.session


def clear_db():
    db.drop_all()
    db.create_all()


def list_users():
    for uid, name in session.query(User.id, User.name):
        print(uid, name)


def add_user():
    user = User(name=fake.name())
    session.add(user)
    session.commit()
    return user.id
