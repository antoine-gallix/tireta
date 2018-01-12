from pdb import set_trace as bp
from pytest import fixture, mark
from flask import current_app
from .utils import is_in
from .db_utils import add_note, add_user
import json
import tireta
import json
import random
import string
from .conftest import build_user_payload, build_note_payload


pytestmark = mark.usefixtures("clear_db")

# ---------------------CLIENT--------------------------


def test_client_exist(client):
    assert client is not None

# ---------------------USER--------------------------


def test_user_resource_exist(client):
    response = client.get('/api/users')
    assert response.status_code == 200


def test_test_start_with_no_user(client):
    response = client.get('/api/users')
    assert response.load() == []


def test_get_non_existing_user(client):
    response = client.get('/api/users/1000')
    assert response.status_code == 404


def test_user_post_user(client):
    payload = build_user_payload()
    response = client.post('/api/users', data=payload)
    assert response.status_code == 201
    response_user = response.load()
    assert is_in(payload, response_user)
    assert response_user['notes'] == []


def test_get_user(client):
    user = add_user()
    response = client.get('/api/users/{}'.format(user.id))
    assert response.status_code == 200


def test_delete_user(client):
    user = add_user()
    user_endpoint = '/api/users/{}'.format(user.id)
    response = client.delete(user_endpoint)
    assert response.status_code == 204
    response = client.get(user_endpoint)
    assert response.status_code == 404


def test_delete_nonexisting_user(client):
    user_endpoint = '/api/users/1'
    response = client.delete(user_endpoint)
    assert response.status_code == 404


# ---------------------NOTES--------------------------


def test_note_resource_exist(client):
    response = client.get('/api/notes')
    assert response.status_code == 200


def test_test_start_with_no_note(client):
    response = client.get('/api/notes')
    assert response.load() == []


def test_get_non_existing_note(client):
    response = client.get('/api/notes/1000')
    assert response.status_code == 404


def test_note_post_note(client):
    user = add_user()
    payload = build_note_payload(user_id=user.id)
    response = client.post('/api/notes', data=payload)
    assert response.status_code == 201


def test_get_note(client):
    user = add_user()
    note = add_note(user)
    response = client.get('/api/notes/{}'.format(note.id))
    assert response.status_code == 200


def test_delete_note(client):
    user = add_user()
    note = add_note(user)
    note_url = '/api/notes/{}'.format(note.id)
    response = client.delete(note_url)
    assert response.status_code == 204
    response = client.get(note_url)
    assert response.status_code == 404

# # ---------------------NOTES WITH TAGS--------------------------


def test_tag_resource_exist(client):
    response = client.get('/api/tags')
    assert response.status_code == 200


def test_test_start_with_no_tag(client):
    response = client.get('/api/tags')
    assert response.load() == []


def test_get_non_existing_tag(client):
    response = client.get('/api/tags/1000')
    assert response.status_code == 404


def test_get_tag(client):
    user = add_user()
    note = add_note(user)
    response = client.get('/api/tags/{}'.format(note.tags[0].id))
    assert response.status_code == 200
