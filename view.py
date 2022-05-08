from main import app
from controller import *

from flask import render_template, request, redirect


@app.route('/')
def index():
    return render_template('notes.html', notes=cntl_select_notes())


@app.route('/note/<int:idx>')
def show_note(idx):
    return render_template('note.html', note=cntl_select_note(idx))


@app.route('/note/<int:idx>/delete')
def delete_note(idx):
    note = cntl_select_note(idx)
    redirect('/')


@app.route('/note/<int:idx>/update', methods=['POST', 'GET'])
def update_note(idx):
    if request.method == 'POST':
        redirect(f'/note/{idx}')
    else:
        return render_template('note-update.html', note=cntl_select_note(idx))


@app.route('/create-note', methods=['POST', 'GET'])
def create_note():
    if request.method == 'POST':
        if cntl_create_note(request.form['title'],
                            request.form['tag'],
                            request.form['text']):
            redirect('/')
        else:
            return render_template('_fatal.html',
                                   error='Не удалось добавить заметку в базу данных')
    else:
        return render_template('note-create.html')
