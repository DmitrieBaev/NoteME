from model import Note, db


def cntl_select_notes():
    """
    Выбор всех заметок

    :return: Список всех заметок, отсортированный по дате модификации по убыванию
    """
    return Note.query.order_by(Note.n_date_m.desc()).all()


def cntl_select_note(id: int):
    """
    Выбор определенной заметки

    :param id: Идентификатор заметки
    :return:
    """
    return Note.query.get(id)


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
        return True
    except Exception:
        return False


def cntl_delete_note(title: str, tag: str, body: str):
    pass


def cntl_update_note(title: str, tag: str, body: str):
    pass
