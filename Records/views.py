from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializer import *

class EmergencyContactViewSet(ModelViewSet):
    queryset = EmergencyContact.objects.select_related('patient__user').select_related('patient').all()
    serializer_class = EmergencyContactSerializer
    
class VisitViewSet(ModelViewSet):
    queryset = Visits.objects.select_related('patient__user').select_related('patient').select_related('doctor').select_related('nurse').all()
    serializer_class = VisitsSerializer

class SurgeryViewSet(ModelViewSet):
    queryset = SurgeryInfo.objects.select_related('patient__user').select_related('patient').select_related('doctor').all()
    serializer_class = SergeryInfoSerializer

class VitalViewSet(ModelViewSet):
    queryset = Vitals.objects.select_related('patient__user').select_related('patient').all()
    serializer_class = VitalSerializer

class MedicalRecordViewSet(ModelViewSet):
    queryset = MedicalRecord.objects.select_related('patient__user').select_related('patient').all()
    serializer_class = MedicalRecordSerializer
# Create your views here.
