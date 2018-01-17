"""A client to interact with tireta server
"""
import requests
from .text_lib import read_note
import logging
from pdb import set_trace as bp
import json

server_port = 'http://localhost:5000'

# Function and command declaration are separated
# so functions can be unit tested


def send_note(file_path, user_id):
    # bp()
    print('file path : ', file_path)
    payload = read_note(file_path)
    url = '/'.join([server_port, 'api', 'users', str(user_id), 'notes'])
    print('url : ', url)
    response = requests.post(url, json=payload)
    if response.ok:
        print('note send successfully')
    else:
        print('note upload failed')


def create_user(user_name):
    print('creating user with name {}'.format(user_name))
    payload = {'name': user_name}
    url = '/'.join([server_port, 'api', 'users'])
    print('url : ', url)
    response = requests.post(url, json=payload)
    if response.ok:
        data = json.loads(response.json())
        print('user created successfully')
        return data['id']
    else:
        print('user creation failed')
