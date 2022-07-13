"""
NoteME URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),  # token/login/ and token/logout

    path('api/v1/', include('notes.urls')),  # ^api/v1/notes/...
    path('api/v1/', include('authors.urls')),  # ^api/v1/profile/...

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
