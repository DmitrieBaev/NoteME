""" Custom urls for authors app """

from django.urls import path, include
from rest_framework import routers

from .views import ProfilesViewSet


profileRouter = routers.SimpleRouter()
profileRouter.register(r'profiles', ProfilesViewSet, basename='profiles')

urlpatterns = [
    path('', include(profileRouter.urls)),
]
