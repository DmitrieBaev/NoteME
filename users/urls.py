"""
Auth URL Configuration
"""
from django.urls import path, include

from .views import *


urlpatterns = [
        path('', index, name='index'),
        path('signup/', sign_up, name='signup'),
        path('login/', sign_in, name='login'),
        path('logout/', sign_out, name='logout'),
        path('profile/', sign_up, name='profile'),
        path('profile/change-avatar/', sign_up, name='profile_change_avatar'),
        path('profile/delete/', sign_up, name='delete_profile'),
        path('change_password/', sign_up, name='change_password'),
        path('reset_password/', sign_up, name='reset_password'),
        path('edit/', sign_up, name='edit_user'),
]
#
# path('', include('django.contrib.auth.urls')) will include the following URL patterns:
#
# login/                    [name='login']
# logout/                   [name='logout']
# password_change/          [name='password_change']
# password_change/done/     [name='password_change_done']
# password_reset/           [name='password_reset']
# password_reset/done/      [name='password_reset_done']
# reset/<uidb64>/<token>/   [name='password_reset_confirm']
# reset/done/               [name='password_reset_complete']
