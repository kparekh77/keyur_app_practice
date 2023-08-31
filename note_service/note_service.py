from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate note storage
notes = []
class NoteService:
    # @app.route('/create_note', methods=['POST'])
    notes = []
    def create_note(self, title, content):
        title = request.form.get('title')
        content = request.form.get('content')
        notes.append({'title': title, 'content': content})
        return jsonify({'message': 'Note created successfully'})

    # @app.route('/get_notes', methods=['GET'])
    def get_notes(self):
        return {'notes': notes}
