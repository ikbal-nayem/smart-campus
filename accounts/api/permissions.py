from accounts.models import Administrator
from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS
)

def is_admin(user, admin_type='admin'):
    check = Administrator.objects.filter(pk=user.id)
    if check.exists():
        if admin_type == 'super':
            return True if check.first().administrator_type == 'Super Admin' else False
        return True if check.first().administrator_type == 'Admin' else False


class IsOwnerOrReadOnly(BasePermission):
    message = "You have no permssion"
    def has_permission(self, request, view):
        if request.user.i_am == 'student':
            return True
        if request.user.i_am == 'teacher' or request.user.i_am == 'staff':
            return eval(f'request.user.{request.user.i_am}info.is_verified')
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj

class IsSuperAdminOrAdmin(BasePermission):
    message = "Admin access only."
    def has_permission(self, request, view):
        return is_admin(request.user) or is_admin(request.user, admin_type='super')
    def has_object_permission(self, request, view, obj):
        if request.user.i_am == 'teacher':
            if eval(f'obj.{obj.i_am}info.department') == request.user.teacherinfo.department:
                return is_admin(request.user) or is_admin(request.user, admin_type='super')

class IsTeacherOrOwner(BasePermission):
    message = "Permission denied, teacher and owner acccess only"
    # def has_permission(self, request, view):
        # if is_admin(request.user, admin_type='super') or is_admin(request.user):
        #     return True
        # if request.user.i_am == 'teacher':
        #     return request.user.teacherinfo.is_verified
    def has_object_permission(self, request, view, obj):
        if is_admin(request.user, admin_type='super') or request.user==obj:
            return True
        if request.user.i_am == 'teacher':
            if eval(f'obj.{obj.i_am}info.department') == request.user.teacherinfo.department:
                if is_admin(request.user):
                    return True
                return request.user.teacherinfo.is_verified
