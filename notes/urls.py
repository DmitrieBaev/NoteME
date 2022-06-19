"""
NoteME (APP) URL Configuration
"""
from django.urls import path

from .views import NoteDetail, NotesList, NotesByCategoryList, NoteCreate, note_new, NoteUpdate, NoteDelete


urlpatterns = [
        path('',            NotesList.as_view( ),   name='notes'),
        path('<int:pk>',    NoteDetail.as_view(),   name='note_detail'),
        path('new/',        NoteCreate.as_view(),               name='note_create'),
        path('category/<int:category_id>', NotesByCategoryList.as_view( ), name='category')
        # path('edit/',       NoteUpdate.as_view(),   name='note_update'),
        # path('delete/',     NoteDelete.as_view(),   name='note_delete'),
]
