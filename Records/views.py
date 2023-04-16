from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializer import *

class EmergencyContactViewSet(ModelViewSet):
    serializer_class = EmergencyContactSerializer

    def get_queryset(self):
        try:
            return EmergencyContact.objects.select_related('patient__user').filter(patient_id = self.kwargs['patient_pk'])
        except KeyError:
            return EmergencyContact.objects.select_related('patient__user').all()
    
    def get_serializer_context(self):
        try:
            return {'patient_id':self.kwargs['patient_pk']}
        except KeyError:
             pass 
     
class VisitViewSet(ModelViewSet):
    serializer_class = VisitsSerializer

    def get_queryset(self):
        try:
            return Visits.objects.select_related('patient__user').select_related('nurse__user').select_related('doctor__user').filter(patient_id = self.kwargs['patient_pk'])
        except KeyError:
            return Visits.objects.select_related('patient__user').select_related('nurse__user').select_related('doctor__user').all()
        
    def get_serializer_context(self):
        try:
            return {'patient_id':self.kwargs['patient_pk'],'doctor_id':self.kwargs['doctor_pk'],'nurse_id':self.kwargs['nurse_pk']}
        except KeyError:
            pass
    
class SurgeryViewSet(ModelViewSet):
    serializer_class = SergeryInfoSerializer
    
    def get_queryset(self):
        try:
            return SurgeryInfo.objects.select_related('patient__user').select_related('doctor__user').filter(patient_id = self.kwargs['patient_pk'])
        except KeyError:
            return SurgeryInfo.objects.select_related('patient__user').select_related('doctor__user').all()
        
    def get_serializer_context(self):
        try:
            return {'patient_id':self.kwargs['patient_pk']}
        except KeyError:
            return {'patient_id':'none'}
   

class VitalViewSet(ModelViewSet):
    serializer_class = VitalSerializer

    def get_queryset(self):
        try:
            return Vitals.objects.select_related('patient__user').filter(patient_id = self.kwargs['patient_pk'])
        except KeyError:
            return Vitals.objects.select_related('patient__user').all()
    
    def get_serializer_context(self):
        try:
            return {'patient_id':self.kwargs['patient_pk']}
        except KeyError:
            pass

class MedicalRecordViewSet(ModelViewSet):
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        try:
            return MedicalRecord.objects.select_related('patient__user').select_related('patient').filter(patient_id=self.kwargs['patient_pk'])
        except KeyError:
            return MedicalRecord.objects.select_related('patient__user').select_related('patient').all()
        
    def get_serializer_context(self):
        try:
            return {'patient_id':self.kwargs['patient_pk']}
        except KeyError:
            pass
# Create your views here.
