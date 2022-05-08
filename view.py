from main import app
from controller import *

from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html', notes=cntl_select_notes())


@app.route('/note/<int:id>')
def show_note(id):
    return render_template('note.html', note=cntl_select_note(id))


@app.route('/create-note', methods=['POST', 'GET'])
def create_note():
    if request.method == 'POST':
        cntl_create_note(request.form['title'],
                         request.form['tag'],
                         request.form['text'])
    else:
        return render_template('note-create.html')
