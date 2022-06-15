from django.contrib import admin

from .models import Note, Category, User


admin.site.register(Note)
admin.site.register(Category)
admin.site.register(User)
