"""
NoteME URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),  # token/login/ and token/logout

    path('api/v1/', include('notes.urls')),  # ^api/v1/notes/...
    path('api/v1/', include('authors.urls')),  # ^api/v1/profile/...
]
