from rest_framework import permissions


class DenyAny(permissions.BasePermission):
    message = "Not Allowed"

    def has_permission(self, request, view):
        return False
