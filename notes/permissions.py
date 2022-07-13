""" Custom permissions for notes app """

from rest_framework import permissions


class NotesCustomPermissions(permissions.BasePermission):
    """
    Granted permissions depends on which view is requesting
    """
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return request.user.is_authenticated
        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if view.action in ['list', 'create']:
            return request.user.is_authenticated
        if view.action == 'retrieve':
            return obj.is_public or obj.created_by == request.user
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.created_by == request.user
        return False
