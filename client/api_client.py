import click
from tireta.client.text_lib import get_note_text, extract_tags

server_port = 'http://localhost:5000'
user_id = 1


@click.command()
def send_note(file_path):
    text = get_note_text(file_path)
    url = '/'.join([server_port, 'api', 'users', user_id, 'notes'])
    print('url : ', url)
    print('text length : ', len(text))
