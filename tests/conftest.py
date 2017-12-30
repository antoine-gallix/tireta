from flask.testing import FlaskClient
from pytest import fixture
from tireta import create_app, db
from faker import Faker
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


@fixture
def app():
    app = create_app()
    app.test_client_class = JSON_Client
    app.app_context().push()
    db.drop_all()
    db.create_all()
    return app


@fixture
def user_id(client):
    """ID of a registered user"""
    payload = build_user()
    response = client.post('/api/user', data=payload)
    return response.json['id']


@fixture
def note_id(client, user_id):
    """ID of a note in the database"""
    payload = build_note(user_id=user_id)
    response = client.post('/api/note', data=payload)
    return response.json['id']
