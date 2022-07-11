from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase

from authors import models


class ProfileModelTest(TestCase):
    """ Класс для тестирования модели с Заметками """

    @classmethod
    def setUp(cls):
        usr = User.objects.create(username='tester',
                                  password='asdz-drqw132.qdQQWE',
                                  last_name='von Everec',
                                  first_name='Olgierd')
        models.Profile.objects.create(user=usr,
                                      bday=date(1272, 11, 9))

    def test_note_string_representation(self):
        """ Правильное строковое представление """
        usr = models.Profile.objects.filter(user__username='tester')
        self.assertEquals(f'tester profile <Olgierd von Everec (1272-11-09)>', str(usr[0]))
