from flask.testing import FlaskClient
from pytest import fixture
from tireta import create_app, db
import data
import json


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


@fixture
def app():
    app = create_app()
    app.test_client_class = JSON_Client
    context = app.app_context()
    context.push()
    db.drop_all()
    db.create_all()
    return app
