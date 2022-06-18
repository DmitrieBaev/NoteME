from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Category(models.Model):
    """
    Класс для таблицы Категория.

    Таблица-справочник, хранит типы категорий заметок.
    Изменять таблицу может только админ.
    """
    
    title = models.SlugField(max_length=100, db_index=True, verbose_name="Категория")
    
    def __str__( self ):
        """ Перегрузка строкового представления класса. """
        # Необходимо для корректного взаимодействия с формой, админкой, выводом значений
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)  # Способ сортировки - ASC по Title


class Note(models.Model):
    """
    Основной класс для таблицы Заметка.
    
    Таблица связана с Категория и Пользователь.
    Автор видит только свои Заметки.
    """
    
    title = models.CharField(max_length=150, db_index=True, verbose_name="Название")
    is_pinned = models.BooleanField(default=False, verbose_name="Закреплена?")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    preview = models.ImageField(upload_to='notes_preview/%Y-%m-%d/', blank=True, verbose_name="Превью")
    body = models.TextField(blank=True, verbose_name="Наполнение")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалена?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Автор")
    
    def get_absolute_url( self ):
        """ Ссылка на объект. """
        
        return reverse_lazy('note_detail', kwargs={ 'pk': self.pk })
    
    def __str__( self ):
        """ Перегрузка строкового представления класса. """
        
        return self.title
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ('-created_at',)  # Способ сортировки - DESC по ДатаСоздания
