from pytest import fixture
from flask import current_app
import json
import tireta


@fixture
def app():
    return tireta.app


def test_client_exist(client):
    assert client is not None


def test_note_put(client):
    note = {'note': 'fligeling'}
    client.put('/note_1000', data=note, content_type='application/json')
    response = client.get('/note_1000')
    assert response.status_code == 200
