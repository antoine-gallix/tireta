from pdb import set_trace as bp
from pytest import fixture, mark
from flask import current_app
from .db_utils import add_note, add_user
import json
import tireta
import json
import random
import string
from .conftest import build_user_payload, build_note_payload


# ---------------------CLIENT--------------------------

def test_client_exist(client):
    assert client is not None


# ---------------------USER--------------------------

def test_user_resource_exist(client):
    response = client.get('/api/user')
    assert response.status_code == 200


def test_test_start_with_no_user(client):
    response = client.get('/api/user')
    assert response.json["num_results"] == 0


def test_get_non_existing_user(client):
    response = client.get('/api/user/1000')
    assert response.status_code == 404


def test_user_post_user(client):
    payload = build_user_payload()
    response = client.post('/api/user', data=payload)
    assert response.status_code == 201


def test_get_user(client):
    user = add_user()
    response = client.get('/api/user/{}'.format(user.id))
    assert response.status_code == 200


def test_delete_user(client):
    user = add_user()
    user_endpoint = '/api/user/{}'.format(user.id)
    response = client.delete(user_endpoint)
    assert response.status_code == 204
    response = client.get(user_endpoint)
    assert response.status_code == 404


# ---------------------NOTES--------------------------


def test_note_resource_exist(client):
    response = client.get('/api/note')
    assert response.status_code == 200


def test_test_start_with_no_note(client):
    response = client.get('/api/note')
    assert response.json["num_results"] == 0


def test_get_non_existing_note(client):
    response = client.get('/api/note/1000')
    assert response.status_code == 404


def test_note_post_note(client):
    user = add_user()
    payload = build_note_payload(user_id=user.id)
    response = client.post('/api/note', data=payload)
    assert response.status_code == 201


def test_get_note(client):
    user = add_user()
    note = add_note(user)
    response = client.get('/api/note/{}'.format(note.id))
    assert response.status_code == 200


def test_delete_note(client):
    user = add_user()
    note = add_note(user)
    note_url = '/api/note/{}'.format(note.id)
    response = client.delete(note_url)
    assert response.status_code == 204
    response = client.get(note_url)
    assert response.status_code == 404

# # ---------------------NOTES WITH TAGS--------------------------


def test_tag_resource_exist(client):
    response = client.get('/api/tag')
    assert response.status_code == 200


def test_test_start_with_no_tag(client):
    response = client.get('/api/tag')
    assert response.json["num_results"] == 0


def test_get_non_existing_tag(client):
    response = client.get('/api/tag/1000')
    assert response.status_code == 404


def test_get_tag(client):
    user = add_user()
    note = add_note(user)
    response = client.get('/api/note/{}'.format(note.tags[0].id))
    assert response.status_code == 200
