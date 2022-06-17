from django.shortcuts import render, redirect
from django.contrib import messages, auth

from .forms import SignUpForm, SignInForm
from .models import Profile


def sign_up( request ):
    """
    Регистрация пользователя
    ---
    Автоматическая авторизация
    Создание профиля
    """
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid( ):
            _user = form.save( )  # Сохранение данных о пользователе
            Profile.objects.create(user=_user)  # Создание профиля пользователя
            auth.login(request, _user)  # Авторизация
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = SignUpForm( )
    return render(request, 'users/signup.html', { "form": form })


def sign_in( request ):
    """ Авторизация и Аутентификация пользователя """

    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid( ):
            _user = form.get_user( )
            auth.login(request, _user)
            messages.success(request, f'С возвращением, <u>{_user.username}</u>!<br/>Рады Вас снова видеть!')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = SignInForm( )
    return render(request, 'users/signin.html', { "form": form })


def sign_out( request ):
    auth.logout(request)
    return redirect('login')


def index( request ):
    """
    Точка входа на сайт.
    
    Проверяет аутентификацию пользователя, если пользователь успешно прошел аутентификацию - перенаправить на основную страницу заметок;
    если пользователь не прошел аутентификацию - перенаправить на страницу Авторизации
    """
    
    user = request.user
    if user.is_authenticated:
        return redirect('login')
    else:
        return redirect('login')
