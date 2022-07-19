""" Custom permissions for authors app """

from rest_framework import permissions


class ProfilesCustomPermissions(permissions.BasePermission):
    """
    Granted permissions depends on which view is requesting
    """
    def has_permission(self, request, view):
        if view.action in ['list']:
            return request.user.is_authenticated
        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        return False  # Access to 'create' denied

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if view.action in ['list']:
            return request.user.is_authenticated
        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return obj.user == request.user
        return False  # Access to 'create' denied
