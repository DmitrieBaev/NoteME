from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm

from .models import Author
from global_helpers import form_helpers


class SignUpForm(UserCreationForm):
    """ Форма регистрации пользователя """
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={ 'class': form_helpers.get_form_controls_class( ) }),
                               help_text=form_helpers.get_form_control_helper('Максимум 150 символов. Только буквы, цифры и символы @/./+/-/_.<br/><b style="color: red">Изменениям не подлежит!</b>'))
    email = forms.EmailField(label='Адрес эл. почты', widget=forms.EmailInput(attrs={ 'class': form_helpers.get_form_controls_class( ) }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={ 'class': form_helpers.get_form_controls_class( ) }),
                                help_text=form_helpers.get_form_control_helper('Минимум 8 символов.<br/>Не должен быть слишком простым и распространенным.<br/>Не может состоять только из цифр.'))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={ 'class': form_helpers.get_form_controls_class( ) }),
                                help_text=form_helpers.get_form_control_helper('Для подтверждения введите, пожалуйста, пароль ещё раз.'))
    
    class Meta:
        model = Author
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={ 'class': form_helpers.get_form_controls_class( )}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={ 'class': form_helpers.get_form_controls_class( ) }))


class PWDChangeForm(PasswordChangeForm):
    pass
