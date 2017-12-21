from pytest import fixture
from tireta import create_app, db


@fixture
def app():
    app = create_app()
    context = app.app_context()
    context.push()
    db.drop_all()
    db.create_all()
    return app
