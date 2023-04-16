from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class EmergencyContactViewSet(ModelViewSet):
    serializer_class = EmergencyContactSerializer

    def get_queryset(self):
        queryset = EmergencyContact.objects.select_related('patient__user').all()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset        

    
    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':str(pateint)}

     
class VisitViewSet(ModelViewSet):
    serializer_class = VisitsSerializer

    def get_queryset(self):
        queryset = Visits.objects.select_related('patient__user').select_related('nurse__user').select_related('doctor__user').all()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset              

        
    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':str(pateint)}

    
class SurgeryViewSet(ModelViewSet):
    serializer_class = SergeryInfoSerializer
    
    def get_queryset(self):
        queryset = SurgeryInfo.objects.select_related('patient__user').select_related('doctor__user').all()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset

    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':str(pateint)}


class VitalViewSet(ModelViewSet):
    serializer_class = VitalSerializer

    def get_queryset(self):
        queryset =  Vitals.objects.select_related('patient__user').all()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset

    
    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':str(pateint)}


class MedicalRecordViewSet(ModelViewSet):
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        queryset = MedicalRecord.objects.select_related('patient__user').select_related('patient').all()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset        

        
    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':str(pateint)}        

