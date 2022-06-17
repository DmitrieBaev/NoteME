from django import forms
from django.contrib.auth import models as auth_models, forms as auth_forms


class SignUpForm(auth_forms.UserCreationForm):
    """ Форма регистрации пользователей """
    
    username = forms.CharField(label='Логин:', max_length=25, widget=forms.TextInput(attrs={ 'class': 'form-control form-control-sm', 'autocomplete': 'off' }),
                               help_text='<small class="form-text text-muted">Максимум 25 символов. Допускаются только буквы, цифры и символы @.+-_</small>')
    email = forms.EmailField(label='Эл. адрес:', widget=forms.EmailInput(attrs={ 'class': 'form-control form-control-sm' }),
                             help_text='<small class="form-text text-muted">Убедитесь, что указываете адрес, к которому у Вас есть доступ.</small>',
                             required=True)
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={ 'class': 'form-control form-control-sm' }))
    password2 = forms.CharField(label='Подтверждение пароля:', widget=forms.PasswordInput(attrs={ 'class': 'form-control form-control-sm' }))
    first_name = forms.CharField(label='Ваше имя:', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'autocomplete': 'off'}), required=True)
    last_name = forms.CharField(label='Ваша Фамилия:', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'autocomplete': 'off'}), required=True)
    
    class Meta:
        model = auth_models.User
        fields = ('username', 'first_name', 'last_name',  'email', 'password1', 'password2')


class SignInForm(auth_forms.AuthenticationForm):
    """ Форма аутентификации пользователя """
    
    username = forms.CharField(label='Логин:', max_length=25, widget=forms.TextInput(attrs={ 'class': 'form-control form-control-sm', 'autocomplete': 'off' }),
                               help_text='<small class="form-text text-muted">Максимум 25 символов. Допускаются только буквы, цифры и символы @.+-_</small>')
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={ 'class': 'form-control form-control-sm' }))


class U4AChangeForm(auth_forms.UserChangeForm):
    """ Форма редактирования пользователя из админки """
    
    first_name = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={ 'class': 'form-control form-control-sm' }))
    last_name = forms.CharField(label='Фамилия пользователя:', widget=forms.TextInput(attrs={ 'class': 'form-control form-control-sm' }))
    
    class Meta:
        model = auth_models.User
        fields = ('first_name', 'last_name')
