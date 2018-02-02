from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        is_admin = request.user.is_staff or request.user.is_superuser

        if request.method in permissions.SAFE_METHODS or is_admin:
            return True
        return obj.user == request.user
