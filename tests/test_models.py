from tireta.models import db
from tireta import create_app
from tireta.models import User, Tag, Note
from pytest import fixture, mark
from pdb import set_trace as bp
import logging

"""Test database models
"""

pytestmark = mark.usefixtures("clear_db")
session = db.session


@fixture(autouse=True, scope='module')
def push_app_context(app):
    """push app context once for tests in the module
    """

    with app.app_context():
        yield


def test_record_user():
    u = User(name='jean-louis')
    session.add(u)
    session.commit()
    assert u.id is not None


def test_record_note_and_user_together():
    u = User(name='jean-louis')
    n = Note(name='things', body='i talk about stuff')
    n.user = u
    session.add(n)
    session.commit()
    assert n.user_id == u.id


def test_record_note_and_user_and_tags_together():
    u = User(name='jean-louis')
    n = Note(name='things', body='i talk about stuff')
    tags = [Tag(name='truc'), Tag(name='chose')]
    n.user = u
    n.tags = tags
    session.add(n)
    session.commit()
    assert n.user_id == u.id
    assert [t.id is not None for t in n.tags]
