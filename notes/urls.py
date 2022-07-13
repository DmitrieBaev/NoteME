""" Custom urls for note app """

from django.urls import path, include
from rest_framework import routers

from .views import NotesViewSet, CategoryReadOnlyViewSet


noteRouter = routers.SimpleRouter()
noteRouter.register(r'notes', NotesViewSet, basename='notes')

categoryRouter = routers.SimpleRouter()
categoryRouter.register(r'categories', CategoryReadOnlyViewSet, basename='categories')

urlpatterns = [
    path('', include(noteRouter.urls)),
    path('', include(categoryRouter.urls)),
]
