from django.db import models

from users.models import Author


class Category(models.Model):
    """
    Класс для таблицы Категория

    Таблица-справочник, хранит типы категорий заметок
    Изменять таблицу может только админ
    """
    title = models.SlugField(max_length=100, db_index=True, verbose_name="Категория")
    
    def __str__(self):
        """ Перегрузка строкового представления класса """
        # Необходимо для корректного взаимодействия с формой и админкой
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)  # Способ сортировки - ASC по Title


class Note(models.Model):
    """
    Основной класс для таблицы Заметка
    
    Таблица связана с Категория и Автор
    Автор видит только свои Заметки
    """
    title = models.CharField(max_length=150, db_index=True,             verbose_name="Название")
    is_pinned = models.BooleanField(default=False,                      verbose_name="Закреплена?")
    category = models.ForeignKey(Category, on_delete=models.PROTECT,    verbose_name="Категория")
    preview = models.ImageField(upload_to='notes_preview/%Y-%m-%d/',    verbose_name="Превью", blank=True)
    body = models.TextField(blank=True,                                 verbose_name="Наполнение")
    is_deleted = models.BooleanField(default=False,                     verbose_name="Удалена?")
    created_at = models.DateTimeField(auto_now_add=True,                verbose_name="Создана в")
    updated_at = models.DateTimeField(auto_now=True,                    verbose_name="Изменена в")
    author = models.ForeignKey(Author, on_delete=models.CASCADE,        verbose_name="Автор")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ('-created_at',)
