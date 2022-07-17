""" Admin settings for note app """

from django.contrib import admin

from .models import Note, Category


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('caption', 'is_pinned', 'is_public', 'modified_at')
    list_editable = ('is_public', 'is_pinned')
    readonly_fields = ('created_by',)
    ordering = ('-modified_at',)
    search_fields = ('caption',)
    list_filter = ('is_public', 'category',)
    filter_horizontal = ('category',)


admin.site.register(Category)
