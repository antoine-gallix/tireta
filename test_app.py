from pdb import set_trace as bp
from pytest import fixture, mark
from flask import current_app
import json
import tireta
import json
import random
import string


@fixture
def app():
    return tireta.app


def make_note_payload():
    return json.dumps({'name': ''.join(random.choices(string.ascii_lowercase, k=5)),
                       'body': ''.join(random.choices(string.ascii_lowercase, k=50))})

# -----------------------------------------------


def test_client_exist(client):
    assert client is not None


def test_no_notes_at_startup(client):
    response = client.get('/api/note')
    assert response.json["num_results"] == 0


def test_get_non_existing_note(client):
    response = client.get('/api/note/1000')
    assert response.status_code == 404


def test_note_post_note(client):
    response = client.post('/api/note', data=make_note_payload(),
                           content_type='application/json')
    assert response.status_code == 201


@mark.dev
def test_note_and_get(client):
    response = client.post('/api/note', data=make_note_payload(),
                           content_type='application/json')
    assert response.status_code == 201
    note_id = response.json['id']
    response = client.get(f'/api/note/{note_id}')
    assert response.status_code == 200
