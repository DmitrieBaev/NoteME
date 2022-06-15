"""
NoteME (APP) URL Configuration
"""
from django.urls import path

from .views import NoteDetail, NotesList, NoteCreate, NoteUpdate, NoteDelete


urlpatterns = [
    path('',            NotesList.as_view(),    name='notes_main'),
    path('<int:pk>',    NoteDetail.as_view(),   name='note_detail'),
    path('new/',        NoteCreate.as_view(),   name='note_create'),
    path('edit/',       NoteUpdate.as_view(),   name='note_update'),
    path('delete/',     NoteDelete.as_view(),   name='note_delete'),
]
