from django.shortcuts import render, redirect
from django.contrib import messages, auth

from .forms import SignUpForm


def sign_up( request ):
    """ Регистрация пользователя с автологином """
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid( ):
            _user = form.save( )
            auth.login(request, _user)
            messages.success(request, 'Регистрация прошла успешно')
            redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    
    else:
        form = SignUpForm( )
    return render(request, 'registration/signup.html', { "form": form })


def index( request ):
    """
    Точка входа на сайт.
    
    Проверяет аутентификацию пользователя, если пользователь успешно прошел аутентификацию - перенаправить на основную страницу заметок;
    если пользователь не прошел аутентификацию - перенаправить на страницу Авторизации
    """
    
    user = request.user
    if user.is_authenticated:
        return redirect('notes')
    else:
        return redirect('login')
