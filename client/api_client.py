import click
import requests
from text_lib import read_note
from pdb import set_trace as bp

server_port = 'http://localhost:5000'
user_id = 1


@click.command()
@click.argument('file_path',
                type=click.Path(exists=True, file_okay=True, readable=True))
def send_note(file_path):
    print('file path : ', file_path)
    payload = read_note(file_path)
    url = '/'.join([server_port, 'api', 'users', str(user_id), 'notes'])
    print('url : ', url)
    reponse = requests.post(url, json=payload)
    print('note send successfully')

if __name__ == '__main__':
    send_note()
