from rest_framework.permissions import BasePermission, SAFE_METHODS


class CanAccess(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and ( 
        hasattr(request.user, 'patient') or 
        hasattr(request.user, 'receptionist') or 
        hasattr(request.user, 'doctor')
        )

class CreateDoctorScheduleOrUpdate(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and hasattr(request.user, 'receptionist')



class BookAppointment(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (hasattr(request.user, 'patient') or hasattr(request.user, 'receptionist'))
        
    