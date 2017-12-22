from pdb import set_trace as bp
import flask
import flask_restless
import flask_sqlalchemy
from config import config

api = flask_restless.APIManager()
db = flask_sqlalchemy.SQLAlchemy()


def create_app(config_name='default'):
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    api.init_app(app=app, flask_sqlalchemy_db=db)
    from models import Note, User
    api.create_api(Note, methods=['GET', 'POST', 'DELETE'])
    api.create_api(User, methods=['GET', 'POST', 'DELETE'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
