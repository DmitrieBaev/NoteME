from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm
from .models import Author


class AuthorAdmin(UserAdmin):
    add_form = SignUpForm
    model = Author
    list_display = ('email', 'username', 'first_name', 'last_name')
    list_editable = ('first_name', 'last_name')


admin.site.register(Author, AuthorAdmin)
