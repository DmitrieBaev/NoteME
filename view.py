from main import app
from controller import *

from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-note', methods=['POST', 'GET'])
def create_note():
    if request.method == 'POST':
        cntl_create_note(request.form['title'],
                         request.form['tag'],
                         request.form['text'])
    else:
        return render_template('create-note.html')
