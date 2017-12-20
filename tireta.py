from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

notes = {}


class Note(Resource):

    def get(self, note_id):
        return {note_id: notes[note_id]}

    def put(self, note_id):
        app.logger.debug(request.data)
        data = request.get_json()
        notes[note_id] = data['note']
        return {note_id: notes[note_id]}


api.add_resource(Note, '/<string:note_id>')

if __name__ == '__main__':
    app.run(debug=True)
