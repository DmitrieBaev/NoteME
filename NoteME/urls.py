"""
NoteME URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from notes import views as v


noteRouter = routers.SimpleRouter()
noteRouter.register(r'notes', v.NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(noteRouter.urls)),
    path('api/v1/notes/', include('notes.urls'))
]
