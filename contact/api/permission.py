from rest_framework import permissions

class IsChannelPartner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_channel_partner



class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow administrators to edit it.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
