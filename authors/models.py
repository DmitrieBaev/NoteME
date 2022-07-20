""" Models for authors app """

from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    return f'users/avatars/{filename}'


class Profile(models.Model):
    """ Profile model """
    user = models.OneToOneField(User, verbose_name='Автор', on_delete=models.CASCADE, primary_key=True)
    bday = models.DateField(verbose_name='Дата рождения')
    avatar = models.ImageField(verbose_name='Превью', upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        """ String representation for profile model """
        return f'{self.user.username} profile <{self.user.first_name} {self.user.last_name} ({self.bday})>'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('pk',)
