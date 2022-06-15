from django.contrib import admin

from .models import Note, Category


class NoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_pinned', 'category', 'preview', 'body', 'is_deleted', 'created_at', 'updated_at')
    list_display_links = ('pk', 'title')
    list_editable = ('is_pinned', 'is_deleted')
    list_filter = ('is_pinned', 'is_deleted', 'category')
    search_fields = ('title',)
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('pk', 'title')
    search_fields = ('title',)


admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
