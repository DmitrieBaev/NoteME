""" Custom permissions for notes app """

from rest_framework import permissions


class IsOwnerOrPublic(permissions.BasePermission):
    """
    Доступ разрешен только владельцу, если заметка не публичная.
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user or obj.is_public


class IsOwner(permissions.BasePermission):
    """
    Доступ разрешен только владельцу.
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user