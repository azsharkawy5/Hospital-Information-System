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


class IsReceptionist(BasePermission):

    def has_permission(self, request, view):
        print(request.user.role)
        return bool(request.user.role =='receptionist' and  request.user)
    

class IsReceptionistOrPatientDoctorReadOnly(BasePermission):
     
    def has_permission(self, request, view):
        return bool(
            request.user.role == 'receptionist' or
            request.user.role == 'patient' and request.method == 'GET' 
            or request.user.role == 'doctor' and request.method == 'GET' 
            #request.method in ('GET', 'HEAD', 'OPTIONS') 
        )
    
class IsReceptionistOrReadOnly(BasePermission):
     
    def has_permission(self, request, view):
        return bool(
            request.user.role == 'receptionist' or
            request.method in ('GET', 'HEAD', 'OPTIONS') 
        )
    

class IsMedicalSecretary(BasePermission):

    def has_permission(self, request, view):
        print(request.user.role)
        return bool(request.user.role =='medical_secretary' and  request.user)
    

class IsMedicalSecretaryOrReadOnly(BasePermission):
     
    def has_permission(self, request, view):
        return bool(
            request.user.role == 'medical_secretary' or
            request.method in ('GET', 'HEAD', 'OPTIONS') 
        )

class IsMedicalSecretaryOrPatientDoctorReadOnly(BasePermission):
     
    def has_permission(self, request, view):
        return bool(
            request.user.role == 'medical_secretary' or
            request.user.role == 'patient' and request.method == 'GET' 
            or request.user.role == 'doctor' and request.method == 'GET' 
            #request.method in ('GET', 'HEAD', 'OPTIONS') 
        )