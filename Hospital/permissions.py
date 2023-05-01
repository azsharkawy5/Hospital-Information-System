from rest_framework.permissions import BasePermission

class IsPatient(BasePermission):

    def has_permission(self, request, view):
        print(request.user.role)
        return bool(request.user.role =='patient' and  request.user)
    

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role)
        return bool(request.user.role =='doctor' and  request.user)   
    
class IsAdminOrReadOnly(BasePermission):
     
     def has_permission(self, request, view):
        return bool(
            request.user.role == 'admin' or
            request.method in ('GET', 'HEAD', 'OPTIONS') 
        )
     

class IsPatientOrReadOnly(BasePermission):
     
    def has_permission(self, request, view):
        return bool(
            request.user.role == 'patient' or
            request.method in ('GET', 'HEAD', 'OPTIONS') 
        )
