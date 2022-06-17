"""
NoteME (PROJECT) URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('admin/', admin.site.urls),
        path('notes/', include('notes.urls')),
        path('', include('users.urls')),
        path('', include('pages.urls')),
]

# DEBUG-only url settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
