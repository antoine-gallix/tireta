import flask
import flask_sqlalchemy
import flask_restless
import json
from pathlib import Path
from flask.testing import FlaskClient

here = Path(__file__).resolve().parent

db = flask_sqlalchemy.SQLAlchemy()
api = flask_restless.APIManager()


class JSON_Client(FlaskClient):
    """Test client that sends json payloads

    instead of:

        test_client.post(some_url,
                        content_type='application/json',
                        data=json.dumps(some_dict))

    just do:

        json_test_client.post(some_url,
                        data=some_dict)

    """

    def open(self, *args, **kwargs):
        if 'data' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data'])
            return super().open(*args, **kwargs,
                                content_type='application/json')
        else:
            return super().open(*args, **kwargs)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body = db.Column(db.Text)


def create_app():
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{here}/tireta.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.test_client_class = JSON_Client

    db.init_app(app)
    api.init_app(app=app, flask_sqlalchemy_db=db)

    api.create_api(Note, methods=['GET', 'POST', 'DELETE'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
