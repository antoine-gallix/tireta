import click
from tireta_client.api_client import send_note as send_note_command
from tireta_client.api_client import create_user as create_user_command


@click.group()
def cli(*args, **kwargs):
    pass


@cli.command()
@click.argument('file_path', type=click.Path(
    exists=True, file_okay=True, readable=True))
@click.argument('user_id', type=click.INT)
def send_note(*args, **kwargs):
    send_note_command(*args, **kwargs)


@cli.command()
@click.argument('user_name', type=click.STRING)
def create_user(*args, **kwargs):
    user_id = create_user_command(*args, **kwargs)
    print(user_id)

cli()
