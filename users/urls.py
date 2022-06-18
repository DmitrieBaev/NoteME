"""
Auth URL Configuration
"""
from django.urls import path, include

from .views import *


urlpatterns = [
        path('', index, name='index'),
        path('signup/', sign_up, name='signup'),
        path('signin/', sign_in, name='signin'),
        path('signout/', sign_out, name='signout'),
        path('profile/', profile, name='profile'),
        path('profile/change-avatar/', change_avatar, name='profile_change_avatar'),
        path('profile/delete/', del_profile, name='delete_profile'),
        path('change_password/', change_pwd, name='change_password'),
        path('reset_password/', reset_pwd, name='reset_password'),
        path('edit/', edit_user, name='edit_user'),
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
