""" Models for notes app """

from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    """ Note model """
    caption = models.CharField(verbose_name='Заголовок', max_length=255, db_index=True)
    body = models.TextField(verbose_name='Текст',blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория', related_name='category', on_delete=models.PROTECT, null=True)
    preview = models.CharField(verbose_name='Превью', max_length=255, default=None)
    is_pinned = models.BooleanField(verbose_name='Закреплена?', default=False)
    is_public = models.BooleanField(verbose_name='Публична?', default=False)
    modified_at = models.DateTimeField(verbose_name='Дата модификации', auto_now=True)
    created_by = models.ForeignKey(User, verbose_name='Автор', related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        """ String representation for note model """
        return self.caption

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ('-modified_at',)


class Category(models.Model):
    """ Note Category model """
    notion = models.CharField(verbose_name='Категория', max_length=255, db_index=True)

    def __str__(self):
        """ String representation for note category model """
        return self.notion

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)
