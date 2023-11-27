from rest_framework.permissions import BasePermission, SAFE_METHODS

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    # def has_permission(self, request, view):
    #     # Check if the user has permission for the entire view
    #     return request.user and request.user.is_authenticated

    # def has_object_permission(self, request, view, obj):
    #     # Check if the user has permission for the specific object
    #     return request.method in ['GET', 'HEAD', 'OPTIONS'] or obj.author == request.user
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user

