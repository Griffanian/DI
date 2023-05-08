from rest_framework import permissions
department_admin = ['miles','zahava']
class IsDepartmentAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.username in department_admin:
            return True
        else:
            return False
