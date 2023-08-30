from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate note storage
notes = []

@app.route('/create_note', methods=['POST'])
def create_note():
    title = request.form.get('title')
    content = request.form.get('content')
    notes.append({'title': title, 'content': content})
    return jsonify({'message': 'Note created successfully'})

@app.route('/get_notes', methods=['GET'])
def get_notes():
    return jsonify({'notes': notes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
