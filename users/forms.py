from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Author


class AuthorCreationForm(UserCreationForm):
    """ Форма регистрации пользователя """

    class Meta:
        model = Author
        fields = ('username', 'email')


class AuthorChangeForm(UserChangeForm):
    """ Форма ?изменения? пользователя """

    class Meta:
        model = Author
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')
