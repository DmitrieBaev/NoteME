"""
Auth URL Configuration
"""
from django.urls import path, include

from .views import SignUpView

urlpatterns = [
        path('', include('django.contrib.auth.urls')),
        path('signup/', SignUpView.as_view(), name='signup')
]
#
# This will include the following URL patterns:
#
# login/                    [name='login']
# logout/                   [name='logout']
# password_change/          [name='password_change']
# password_change/done/     [name='password_change_done']
# password_reset/           [name='password_reset']
# password_reset/done/      [name='password_reset_done']
# reset/<uidb64>/<token>/   [name='password_reset_confirm']
# reset/done/               [name='password_reset_complete']
