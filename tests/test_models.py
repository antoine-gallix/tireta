from tireta import db, app
from pytest import fixture
from pdb import set_trace as bp
import logging

"""Test database models
"""


@fixture
def session():
    session = db.session
    yield session
    session.rollback()


@fixture(autouse=True, scope='module')
def push_app_context():
    with app.app_context():
        yield
