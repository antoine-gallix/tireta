import flask
import flask_restless
from config import config
import data

api = flask_restless.APIManager()


def create_app(config_name='default'):
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])
    data.db.init_app(app)
    api.init_app(app=app, flask_sqlalchemy_db=data.db)

    api.create_api(data.Note, methods=['GET', 'POST', 'DELETE'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
