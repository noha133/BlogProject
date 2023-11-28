# permissions.py
from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()

class AuthorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Author').exists()
    def has_object_permission(self, request, view, obj):
        # Allow the author to update or delete their own posts
        return obj.author == request.user

class ReaderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Reader').exists()
