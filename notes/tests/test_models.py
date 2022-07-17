from django.contrib.auth.models import User
from django.test import TestCase

from notes import models


class NoteModelTest(TestCase):
    """ Класс для тестирования модели с Заметками """

    @classmethod
    def setUp(cls):
        usr = User.objects.create(username='tester',
                                  password='asdz-drqw132.qdQQWE')
        ctgry = models.Category.objects.create(notion='Testing')
        nt = models.Note.objects.create(caption='Test note',
                                        created_by=usr)
        nt.category.add(ctgry)

    def test_note_string_representation(self):
        """ Правильное строковое представление """
        note = models.Note.objects.filter(caption='Test note')
        self.assertEquals('Test note', str(note[0]))

    def test_note_caption_max_length(self):
        """ Правильная длина поля caption """
        note = models.Note.objects.filter(caption='Test note')
        self.assertEquals(note[0]._meta.get_field('caption').max_length, 255)

    def test_note_category_relationship(self):
        """ Отношение Заметка - Категория """
        note = models.Note.objects.filter(caption='Test note').first()
        note_categories = note.category.all().first()
        category = models.Category.objects.filter(notion='Testing').first()
        self.assertEquals(note_categories.notion, category.notion)

    def test_note_user_relationship(self):
        """ Отношение Заметка - User (contrib.auth.models) """
        note = models.Note.objects.filter(caption='Test note').first()
        self.assertEquals(note.created_by.username, 'tester')


class CategoryModelTest(TestCase):
    """ Класс для тестирования модели с Категориями Заметок """

    @classmethod
    def setUp(cls):
        models.Category.objects.create(notion='Testing')

    def test_category_string_representation(self):
        """ Правильное строковое представление """
        ctgry = models.Category.objects.filter(notion='Testing')
        self.assertEquals('Testing', str(ctgry[0]))

    def test_category_notion_max_length(self):
        """ Правильная длина поля caption """
        ctgry = models.Category.objects.filter(notion='Testing')
        self.assertEquals(ctgry[0]._meta.get_field('notion').max_length, 255)
