from model import Note, db

from datetime import datetime


def cntl_select_notes():
    """
    Выбор всех заметок

    :return: Список всех заметок, отсортированный по дате модификации по убыванию
    """
    return Note.query.order_by(Note.n_date_m.desc()).filter(Note.n_deleted == False, Note.n_pinned == False).all()


def cntl_select_pinned_notes():
    """
    Выбор всех закрепленных заметок

    :return: Список всех закрепленных заметок, отсортированный по дате модификации по убыванию
    """
    return Note.query.order_by(Note.n_date_m.desc()).filter(Note.n_deleted == False, Note.n_pinned == True).all()


def cntl_select_note(idx: int):
    """
    Выбор определенной заметки

    :param idx: Идентификатор заметки
    :return:
    """
    return Note.query.get_or_404(idx)


def cntl_create_note(title: str, tag: str, body: str):
    """
    Создание новой заметки

    :param title: Название заметки
    :param tag: Метка для заметки
    :param body: Текст заметки
    """
    note = Note(n_title=title, n_tag=tag, n_tag_preview=f'img/tag_{tag}.jpg', n_body=body)
    try:
        db.session.add(note)
        db.session.commit()
        return True
    except Exception:
        return False


def cntl_delete_note(idx: int):
    """
    Пометить заметку на удаление

    :param idx: Идентификатор заметки
    """
    note = cntl_select_note(idx)
    note.n_date_m = datetime.utcnow()
    note.n_deleted = True
    try:
        db.session.commit()
        return True
    except Exception:
        return False


def cntl_delete_notes():
    """ Удаление помеченных заметок из БД """
    try:
        to_delete = Note.query.filter(Note.n_deleted == True).all()
        db.session.delete(to_delete)
        db.session.commit()
    except Exception:
        db.session.rollback()


def cntl_update_note(idx: int, title: str, tag: str, body: str):
    """
    Изменение заметки

    :param idx: Идентификатор заметки
    :param title: Название заметки
    :param tag: Метка для заметки
    :param body: Текст заметки
    """
    note = cntl_select_note(idx)
    note.n_title = title
    note.n_tag = tag
    note.n_body = body
    note.n_date_m = datetime.utcnow()
    try:
        db.session.commit()
        return True
    except Exception:
        return False


def cntl_pin_note(idx: int):
    """
    Закрепление заметки

    :param idx: Идентификатор заметки
    """
    note = cntl_select_note(idx)
    note.n_date_m = datetime.utcnow()
    note.n_pinned = True
    try:
        db.session.commit()
        return True
    except Exception:
        return False


def cntl_unpin_note(idx: int):
    """
    Открепление заметки

    :param idx: Идентификатор заметки
    """
    note = cntl_select_note(idx)
    note.n_date_m = datetime.utcnow()
    note.n_pinned = False
    try:
        db.session.commit()
        return True
    except Exception:
        return False
