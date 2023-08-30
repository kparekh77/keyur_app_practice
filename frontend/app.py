# frontend/app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = 'http://user_service:5001'
NOTE_SERVICE_URL = 'http://note_service:5002'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    response = requests.post(f'{USER_SERVICE_URL}/register', data={'username': username, 'password': password})
    data = response.json()
    
    if response.status_code == 200:
        return jsonify({'message': 'User registered successfully'})
    else:
        return jsonify({'message': 'User registration failed'})

@app.route('/create_note', methods=['POST'])
def create_note():
    title = request.form.get('title')
    content = request.form.get('content')
    
    response = requests.post(f'{NOTE_SERVICE_URL}/create_note', data={'title': title, 'content': content})
    data = response.json()
    
    if response.status_code == 200:
        return jsonify({'message': 'Note created successfully'})
    else:
        return jsonify({'message': 'Note creation failed'})

@app.route('/get_notes', methods=['GET'])
def get_notes():
    response = requests.get(f'{NOTE_SERVICE_URL}/get_notes')
    data = response.json()
    notes = data['notes']
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
