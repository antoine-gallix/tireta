import flask
import flask_sqlalchemy
import flask_restless
import json
from config import config

db = flask_sqlalchemy.SQLAlchemy()
api = flask_restless.APIManager()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.Text)


def create_app(config_name='default'):
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    api.init_app(app=app, flask_sqlalchemy_db=db)

    api.create_api(Note, methods=['GET', 'POST', 'DELETE'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
