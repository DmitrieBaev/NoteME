from django.db import models
from django.contrib.auth.models import User


def user_dir_path(instance, filename):
    return 'profile/{0}/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
    """
    Класс для таблицы Профиль
    
    Таблица связана с Пользователь
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True, verbose_name="Пользователь")
    avatar = models.ImageField(upload_to=user_dir_path, blank=True, height_field=32, width_field=32, verbose_name="Аватар")
    
    def __str__( self ):
        return f'Профиль {self.user}`a'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
