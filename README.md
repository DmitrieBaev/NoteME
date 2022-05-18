<h1 align="center">NoteME</h1>
<h5 align="center">Приложения для заметок</h5>
</br>

В приложении реализованы базовые возможности взаимодействия с заметками: _добавление_, _редактирование_, _удаление_, _закрепление_, _просмотр_.
Главная страница разделена на две **категории**: закрепленные заметки и все остальные.

![image](https://user-images.githubusercontent.com/47382305/167486706-d53d41de-ceea-4cf4-bb66-0508baa87114.png)

</br>

---

</br>

При создании или редактировании заметки можно выбрать категорию (**метку**).

![image](https://user-images.githubusercontent.com/47382305/167487725-60e26749-e70a-497b-b537-54af5c1a7d3d.png)

Выбор метки реализован во встраивамом шаблоне html-страницы для использования в нескольких других страницах. Такая реализация поможет быстро найти нужный файл для дальнейшего расширения/изменения.

> _tags.html

```html
    <div class="col-12">
        <label for="noteTag" class="form-label">Выберите категорию заметки <b>(метку)</b></label>
        <select class="form-select" name="tag" id="noteTag" required="">
            <option value="other">Другое</option>
            <option value="entertainment">Развлечения</option>
            <option value="furniture">Обстановка (Фурнитура)</option>
            <option value="gardening">Садоводство</option>
            <option value="presents">Подарки</option>
            <option value="purchases">Покупки</option>
            <option value="resting">Отдых</option>
        </select>
        <div class="invalid-feedback">
            Выберите валидную категорию для заметки.
        </div>
    </div>
```

> note-create.html

```html
    <div class="col-md-6">
        {# Встраиваем выбор метки #}
        {% include '_tags.html' %}
    </div>
```

</br>

---

</br>

Удаление заметки реализовано через изменение флага в базе данных. В качестве примера использовалась БД SQLite.
> Физическое удаление можно переложить на функции СУБД, если используется mysql или pgsql

При удалении через интерфейс приложения - в БД "удаляемая" заметка помечается на удаление. А уже после удаляется физически из БД, при выполнении определенного условия, например, `в конце недели` или `если дата модификации была N дней назад`.

```python
def cntl_delete_notes():
    try:
        to_delete = Note.query.filter(Note.n_deleted == True).all()
        db.session.delete(to_delete)
        db.session.commit()
    except Exception:
        db.session.rollback()
```

</br>

---

</br>

Для каждой категории (**метки**) заметки предусмотрено собственное изображение.

![image](https://user-images.githubusercontent.com/47382305/167489409-d7aacec0-7f18-40d0-92f0-da8869b35581.png)

Путь к изображению сохраняется в БД. Для конфигурации пути исползуются значения селектора категорий заметок:

```python
    note = Note(n_title=title,
                n_tag=tag,
                n_tag_preview=f'img/tag_{tag}.jpg',
                n_body=body)
    try:
        db.session.add(note)
        db.session.commit()
        return True
    except Exception:
        return False
```

</br>

---

</br>

Приложение может быть модифицировано реализацией:
- [ ] Переход на mysql/pgsql или noSQL базы данных
- [ ] Добавление авторизации и привязка заметок к пользователю
- [ ] Перенос категорий (**меток**) в таблицу БД с последующей возможностью редактирования
- [X] Возможность _закреплять_ заметки
- [X] Поддержка Markdown разметки для текста заметки

</br>

---

</br>

Скриншоты всех страниц:

1. Добавление заметки:

<p align="right">Было:</p>

![image](https://user-images.githubusercontent.com/47382305/167490840-07490e16-658b-42d2-92b7-f0ab5c91f22e.png)

<p align="right">Стало:</p>

![image](https://user-images.githubusercontent.com/47382305/167492436-e3830227-cc13-4429-8584-0560f9ed76ff.png)

2. Просмотр заметки:

![image](https://user-images.githubusercontent.com/47382305/169108355-170ff8e8-a704-470e-ad6d-2ba82f463039.png)

3. Редактирование заметки:

![image](https://user-images.githubusercontent.com/47382305/169108435-ce79623a-57be-4ed5-a534-b51bbb419ec1.png)
