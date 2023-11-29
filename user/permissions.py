# permissions.py
from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="AdminGroup").exists()


class AuthorPermission(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.groups.filter(name="AuthorGroup").exists()
            | request.user.groups.filter(name="AdminGroup").exists()
        )

    def has_object_permission(self, request, view, obj):
        # Allow the author to update or delete their own posts
        if request.user.groups.filter(name="AuthorGroup").exists():
            return obj.author == request.user
        else:
            return True


class ReaderPermission(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.groups.filter(name="ReaderGroup").exists()
            | request.user.groups.filter(name="AdminGroup").exists()
            | request.user.groups.filter(name="AuthorGroup").exists()
        )
