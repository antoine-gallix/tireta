from flask import Response
from flask.testing import FlaskClient
from pytest import fixture
from time import sleep
from tireta import create_app
from pathlib import Path
from multiprocessing import Process
from tireta.models import db
from faker import Faker
from .db_utils import add_user
import logging
import json

fake = Faker()


def build_note_payload(with_tags=False, **kwargs):
    """Build payload for note creation

    kwargs are added to the payload
    with_tags : add random tags to the payload
    """

    payload = {'name': ' '.join(fake.words()),
               'body': fake.text()}
    payload.update(kwargs)
    if with_tags:
        payload.update({'tags': fake.words()})
    return payload


def build_user_payload():
    """Build payload for user creation

    kwargs are added to the payload
    """
    return {'name': fake.name()}


class JSON_Client(FlaskClient):
    """Test client that sends json payloads

    instead of:

        test_client.post(some_url,
                        content_type='application/json',
                        data=json.dumps(some_dict))

    just do:

        json_test_client.post(some_url,
                        data=some_dict)

    """

    def open(self, *args, **kwargs):
        # encode data into json and set content type
        if 'data' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data'])
            return super().open(*args, **kwargs,
                                content_type='application/json')
        else:
            return super().open(*args, **kwargs)


class Load_JSON_Response(Response):
    """adds a method to the response class to load json
    """

    def load(self):
        return json.loads(self.json)


@fixture(scope='session')
def app():
    application = create_app('test')
    application.test_client_class = JSON_Client
    application.response_class = Load_JSON_Response
    return application


@fixture
def reset_db(app):
    logging.debug('reset db tables')
    db.drop_all()
    db.create_all()


@fixture(scope='module')
def running_server(app):
    """Run the app in a parallel process
    """
    # FIX : reset_db must be used directly as a function,
    # not as a fixture. if not, pytest fixture scope conflict
    reset_db(app)
    app_process = Process(target=app.run)
    logging.debug('running test server')
    app_process.start()
    sleep(.2)
    yield
    app_process.terminate()
    logging.debug('shutting down test server')


@fixture
def user(app, clear_db):
    with app.app_context():
        user = add_user()
    return user


# -----------------------------------------------

# ----| material for building notes in files
TAG_MARK = '#TAGS:'  #  markup sequence for a tag line
TAGS = fake.words()  # a list of word strings
SIMPLE_TEXT = fake.text()  # a string of words

tag_line = TAG_MARK + ','.join(TAGS)
# a line of tag markup, then a text
TAGGED_TEXT = '\n'.join([tag_line, SIMPLE_TEXT])


@fixture
def tmpfile(tmpdir):
    """path to a file in a temporary directory
    """

    file_path = Path(tmpdir / 'test_file')
    return file_path


@fixture
def note_file(tmpfile):
    """file written with a simple text
    """
    tmpfile.write_text(SIMPLE_TEXT)
    return tmpfile


@fixture
def note_file_with_tags(tmpfile):
    """file written with text and a tag line
    """
    tmpfile.write_text(TAGGED_TEXT)
    return tmpfile
