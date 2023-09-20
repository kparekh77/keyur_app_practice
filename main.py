from flask import Flask, render_template, request, jsonify
import requests
from note_service.note_service import NoteService
from user_service.user_service import UserService

app = Flask(__name__)

note_service = NoteService()
user_service = UserService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_note', methods=['POST'])
def create_notes():
    return note_service.create_note(request.form.get('title'), request.form.get('content'))

@app.route('/get_notes', methods=['GET'])
def get_notes():
    data = note_service.get_notes()
    notes = data['notes']
    return render_template('notes.html', notes=notes)

@app.route('/register', methods=['POST'])
def register():
    return user_service.register(request.form.get('username'), request.form.get('password'))

@app.route('/login', methods=['POST'])
def login():
    return user_service.login(request.form.get('username'), request.form.get('password'))

if __name__ == '__main__':
    app.run()