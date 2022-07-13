""" Custom urls for note app """

from django.urls import path, include
from rest_framework import routers

from . import views as v


noteRouter = routers.SimpleRouter()
noteRouter.register(r'notes', v.NotesViewSet, basename='notes')

urlpatterns = noteRouter.urls

# urlpatterns = (
#     path('notes/', v.NotesListCreate.as_view()),
#     path('notes/<int:pk>/', v.NotesRetrieveUpdateDestroy.as_view()),
#     # path('notes/<int:pk>/', v.NotesUpdateDestroy.as_view()),
# )
