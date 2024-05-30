from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if (request.method in ('PUT', 'PATCH') and request.headers.get('userToken') == obj.author or
                request.user.is_staff):
            return True
        if request.method == 'DELETE' and request.user.is_staff:
            return True

        return False
