from main import app
from controller import *

from flask import render_template, request, redirect


# TODO: Шаблон FATAL

@app.route('/')
def index():
    # TODO: Шаблон главной страницы
    return render_template('notes.html',
                           pinned_notes=cntl_select_pinned_notes(),
                           notes=cntl_select_notes())


@app.route('/note/<int:idx>')
def show_note(idx):
    # TODO: Шаблон просмотра заметки
    return render_template('note.html', note=cntl_select_note(idx))


@app.route('/note/<int:idx>/delete')
def delete_note(idx):
    if cntl_delete_note(idx):
        return redirect('/')
    else:
        return render_template('_fatal.html',
                               error='Не удалось изменить заметку в базе данных')


@app.route('/note/<int:idx>/update', methods=['POST', 'GET'])
def update_note(idx):
    # TODO: Шаблон редактирования заметки
    if request.method == 'POST':
        if cntl_update_note(idx=idx,
                            title=request.form['title'],
                            tag=request.form['tag'],
                            body=request.form['text']):
            return redirect(f'/note/{idx}')
        else:
            return render_template('_fatal.html',
                                   error='Не удалось изменить заметку в базе данных')
    else:
        return render_template('note-update.html', note=cntl_select_note(idx))


@app.route('/note/<int:idx>/pin')
def pin_note(idx):
    if cntl_pin_note(idx):
        return redirect('/')
    else:
        return render_template('_fatal.html',
                               error='Не удалось закрепить заметку')


@app.route('/note/<int:idx>/unpin')
def unpin_note(idx):
    if cntl_unpin_note(idx):
        return redirect('/')
    else:
        return render_template('_fatal.html',
                               error='Не удалось открепить заметку')


@app.route('/create-note', methods=['POST', 'GET'])
def create_note():
    if request.method == 'POST':
        if cntl_create_note(title=request.form['title'],
                            tag=request.form['tag'],
                            body=request.form['text']):
            return redirect('/')
        else:
            return render_template('_fatal.html',
                                   error='Не удалось добавить заметку в базу данных')
    else:
        return render_template('note-create.html')
