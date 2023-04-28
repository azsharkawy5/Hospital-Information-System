from rest_framework.permissions import BasePermission

class IsPatient(BasePermission):

    def has_permission(self, request, view):
        print(request.user.role)
        return bool(request.user.role =='patient' and  request.user)