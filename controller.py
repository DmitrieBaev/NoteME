from model import Note, db
from flask import redirect


def cntl_create_note(title: str, tag: str, body: str):
    """
    Создание новой заметки

    :param title: Название заметки
    :param tag: Метка для заметки
    :param body: Текст заметки
    """
    note = Note(n_title=title, n_tag=tag, n_body=body)
    try:
        db.session.add(note)
        db.session.commit()
    except Exception:
        # Добавить обработку исключений
        pass
    finally:
        return redirect('/')
