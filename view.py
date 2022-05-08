from main import app
from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-note', methods=['POST', 'GET'])
def create_note():
    if request.method == 'POST':
        pass
    else:
        return render_template('create-note.html')
