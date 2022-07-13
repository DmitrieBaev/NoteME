""" Custom urls for note app """

from rest_framework import routers

from . import views as v


noteRouter = routers.SimpleRouter()
noteRouter.register(r'notes', v.NotesViewSet, basename='notes')

urlpatterns = noteRouter.urls
