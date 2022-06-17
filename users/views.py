from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate

from .forms import SignUpForm


class SignUpView(CreateView):
    """ Контроллер регистрации """
    
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    
    def form_valid( self, form ):
        """ Валидация формы с автологином """
        
        login(self.request, authenticate(username=form.cleaned_data['username'],
                                         password=form.cleaned_data['password1']))
        return super( ).form_valid(form)
