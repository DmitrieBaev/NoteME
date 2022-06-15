from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path( instance, filename ):
    """
    Кастомный каталог для сохранения пользовательских аватаров.\n
    Файл будет загружен в MEDIA_ROOT/user_<id>/<filename>

    :return: Строка вида `user_1/avabomb.png`
    """
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Author(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, blank=True,
                               width_field=500, height_field=500,
                               verbose_name='Аватар')

    def __str__( self ):
        return self.username
