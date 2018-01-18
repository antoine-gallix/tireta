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
    logging.info('sending note : '.format(file_path))
    payload = read_note(file_path)
    url = '/'.join([server_port, 'api', 'users', str(user_id), 'notes'])
    logging.info('to url : {}'.format(url))
    response = requests.post(url, json=payload)
    if response.ok:
        data = json.loads(response.json())
        logging.info('note send successfully')
        return data
    else:
        logging.error('note upload failed')


def create_user(user_name):
    logging.info('creating user with name {}'.format(user_name))
    payload = {'name': user_name}
    url = '/'.join([server_port, 'api', 'users'])
    logging.info('url : {}'.format(url))
    response = requests.post(url, json=payload)
    if response.ok:
        data = json.loads(response.json())
        logging.info('user created successfully')
        return data
    else:
        logging.error('user creation failed')
