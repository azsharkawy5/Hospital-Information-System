from .models import *
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializer import *
from Hospital.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class EmergencyContactViewSet(ModelViewSet):
    serializer_class = EmergencyContactSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name','last_name']
    permission_classes = [IsPatientOrReadOnly]
    def get_queryset(self):
        if self.request.user.role=='patient':
            return EmergencyContact.objects.filter(patient__user=self.request.user).select_related('address').all()
        return EmergencyContact.objects.select_related('address').all()
    def get_serializer_context(self):
        return {'user':self.request.user}




     
class VisitViewSet(ModelViewSet):
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['admission_date','discharge_date']
    search_fields = ['doctor__user__first_name','doctor__user__last_name','patient__user__first_name','patient__user__last_name']
    serializer_class = VisitsSerializer
    permission_classes = [IsReceptionistOrReadOnly]
    def get_queryset(self):
        if self.request.user.role == 'patient':
            return Visits.objects.select_related('patient').select_related('doctor').filter(patient__user=self.request.user).all()
        elif self.request.user.role == 'doctor':
            return Visits.objects.select_related('patient').select_related('doctor').filter(doctor__user=self.request.user).all()
        return Visits.objects.select_related('patient').select_related('doctor').all()


    
class SurgeryViewSet(ModelViewSet):
    serializer_class = SergeryInfoSerializer
    
    def get_queryset(self):
        queryset = SurgeryInfo.objects.select_related('patient__user').select_related('doctor__user').all() 
        patient_id = self.kwargs.get('patient_pk')
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
        patient_id = self.kwargs.get('patient_pk')
        print(patient_id)
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset

    
    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':pateint}


class MedicalRecordViewSet(ModelViewSet):
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        queryset = MedicalRecord.objects.select_related('patient__user').all()
        patient_id = self.kwargs.get('patient_pk')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset        

        
    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':str(pateint)}        

class PatientRecordsViewSet(ReadOnlyModelViewSet):
    queryset = Patient.objects.select_related('patient_record').prefetch_related('patient_vital').prefetch_related('patient_surgery').prefetch_related('patient_surgery').prefetch_related('inpatient').all()
    serializer_class = PatientAllRecordrSerializer
     

