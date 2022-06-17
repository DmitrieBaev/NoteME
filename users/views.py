from django.urls import reverse_lazy
from django.views.generic import DetailView, edit
from django.contrib.auth import login, views, authenticate

from .forms import SignUpForm, SignInForm, PWDChangeForm


class SignUpView(edit.CreateView):
    """ Контроллер регистрации """
    form_class = SignUpForm
    template_name = 'users/signup.html'
    
    def form_valid( self, form ):
        """ Валидация формы """
        # Автологин после регистрации
        login(self.request, authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1']))  # => login(self.request, self.object) without authenticate
        return super( ).form_valid(form)


class SignInView(views.LoginView):
    """ Контроллер авторизации пользователя """
    form_class = SignInForm
    template_name = 'users/signin.html'


class SignOutView(views.LogoutView):
    """ Контроллер авторизации пользователя """
    pass


class PWDChangeView(views.PasswordChangeView):
    """ Контроллер смены пароля """
    form_class = PWDChangeForm
    success_url = reverse_lazy('index')
    template_name = 'users/edit_pwd.html'
