""" Custom urls for note app """

from django.urls import path

from . import views as v


urlpatterns = [
    path('notes/', v.NotesList.as_view()),
    path('notes/<int:pk>/', v.NotesRetrieve.as_view()),
    path('notes/<int:pk>/edit/', v.NotesUpdateDestroy.as_view()),
]
