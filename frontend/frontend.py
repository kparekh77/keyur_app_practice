# frontend/app.py
from flask import Flask, render_template, request, jsonify
import requests
from note_service.note_service import NoteService
app = Flask(__name__)

# @app.route('/')
class FrontEnd:
    
    def index():
        return render_template('index.html')

    # @app.route('/get_notes', methods=['GET'])
    def get_notes():
        data = NoteService.get_notes()
        notes = data['notes']
        return render_template('notes.html', notes=notes)
