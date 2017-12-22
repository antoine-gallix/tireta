from pdb import set_trace as bp
from pytest import fixture, mark
from flask import current_app
import json
import tireta
import json
import random
import string


def random_word(nb_letters):
    return ''.join(random.choices(string.ascii_lowercase, k=nb_letters))


def random_text(nb_words, word_length=5):
    return ' '.join([random_word(word_length) for _ in range(nb_words)])


def build_note(**kwargs):
    """Build payload for note creation

    kwargs are added to the payload
    """

    payload = {'name': random_text(3),
               'body': random_text(50)}
    payload.update(kwargs)
    return payload


def build_user():
    """Build payload for user creation

    kwargs are added to the payload
    """
    return {'name': ''.join(random.choices(string.ascii_lowercase, k=5))}


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


@mark.dev
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
