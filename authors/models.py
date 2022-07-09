""" Models for authors app """

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """ Profile model """
    user = models.OneToOneField(User, verbose_name='Автор', on_delete=models.CASCADE, primary_key=True)
    bday = models.DateTimeField(verbose_name='Дата рождения')
    avatar = models.CharField(verbose_name='Аватар', max_length=255, default=None)

    def __str__(self):
        """ String representation for profile model """
        return f'{self.user.username} profile <{self.user.last_name} {self.user.first_name} ({self.bday})>'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('pk',)
