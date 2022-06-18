from django.shortcuts import render, redirect
from django.contrib import messages, auth

from .forms import SignUpForm, SignInForm, NamesChangeForm
from .models import Profile


def sign_up( request ):
    """
    Регистрация пользователя.
    ---
    Автоматическая авторизация.
    Создание профиля.
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
        # Редирект на профиль пользователя, если пользователь авторизирован
        if request.user.is_authenticated:
            return redirect('profile')
        # Иначе показать форму регистрации
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
        # Редирект на профиль пользователя, если пользователь авторизирован
        if request.user.is_authenticated:
            return redirect('profile')
        # Иначе показать форму авторизации
        form = SignInForm( )
    return render(request, 'users/signin.html', { "form": form })


def sign_out( request ):
    auth.logout(request)
    return redirect('signin')


def edit_user( request ):
    """ Изменение персональных данных пользователя (Имя/Фамилия) """
    
    if request.method == 'POST':
        form = NamesChangeForm(request.POST, instance=request.user)
        if form.is_valid( ):
            form.save( )
            messages.success(request, f'Данные успешно сохранены.')
            return redirect('profile')
        else:
            messages.error(request, 'Не удалось изменить данные.')
    else:
        # Редирект на профиль пользователя, если пользователь авторизирован
        if request.user.is_authenticated:
            return redirect('profile')
        # Иначе показать форму редактирования данных
        form = NamesChangeForm(instance=request.user)
    return render(request, 'users/sign_edit.html', { "form": form })


def profile(request):
    return render(request, 'users/profile.html', {  })


def edit_profile(request):
    pass


def del_profile(request):
    pass


def change_avatar(request):
    pass


def reset_pwd(request):
    pass


def change_pwd(request):
    pass


def index( request ):
    """
    Точка входа на сайт.
    
    Проверяет аутентификацию пользователя, если пользователь успешно прошел аутентификацию - перенаправить на основную страницу заметок;
    если пользователь не прошел аутентификацию - перенаправить на страницу Авторизации
    """
    
    # _user = request.user
    # if _user.is_authenticated:
    #     try:
    #         pfl = Profile.objects.get(user=_user).first()
    #     except Profile.DoesNotExist:
    #         messages.error(request, 'Не удалось загрузить аватар пользователя.')
    #     return render(request, 'users/_profile_block.html', { "avatar": pfl })
    
    # Редирект на страницу с заметками, если пользователь авторизирован
    if request.user.is_authenticated:
        return redirect('profile')
    # Иначе редирект на страницу авторизации
    return redirect('signin')

