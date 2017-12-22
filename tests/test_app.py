from pdb import set_trace as bp
from pytest import fixture, mark
from flask import current_app
import json
import tireta
import json
import random
import string
from faker import Faker
fake = Faker()


def build_note(**kwargs):
    """Build payload for note creation

    kwargs are added to the payload
    """

    payload = {'name': ' '.join(fake.words()),
               'body': fake.text()}
    payload.update(kwargs)
    return payload


def build_user():
    """Build payload for user creation

    kwargs are added to the payload
    """
    return {'name': fake.name()}


@fixture
def user_id(client):
    """ID of a registered user"""
    payload = build_user()
    response = client.post('/api/user', data=payload)
    return response.json['id']

# ---------------------CLIENT--------------------------


def test_client_exist(client):
    assert client is not None

# ---------------------NOTES--------------------------


def test_no_notes_at_startup(client):
    response = client.get('/api/note')
    assert response.json["num_results"] == 0


def test_get_non_existing_note(client):
    response = client.get('/api/note/1000')
    assert response.status_code == 404


def test_note_post_note(client, user_id):
    payload = build_note(user_id=user_id)
    response = client.post('/api/note', data=payload)
    assert response.status_code == 201


def test_post_and_get_note(client, user_id):
    payload = build_note(user_id=user_id)
    response = client.post('/api/note', data=payload)
    assert response.status_code == 201
    note_id = response.json['id']
    response = client.get(f'/api/note/{note_id}')
    assert response.status_code == 200

# ---------------------USER--------------------------


def test_user_resource_exist(client):
    response = client.get('/api/user')
    assert response.status_code == 200


def test_no_users_at_startup(client):
    response = client.get('/api/user')
    assert response.json["num_results"] == 0


def test_get_non_existing_user(client):
    response = client.get('/api/user/1000')
    assert response.status_code == 404


def test_user_post_user(client):
    response = client.post('/api/user', data=build_user())
    assert response.status_code == 201


def test_post_and_get_user(client):
    response = client.post('/api/user', data=build_user())
    assert response.status_code == 201
    user_id = response.json['id']
    response = client.get(f'/api/user/{user_id}')
    assert response.status_code == 200
