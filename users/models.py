from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__( self ):
        return self.username
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('-created_at',)
