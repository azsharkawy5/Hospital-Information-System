from .models import *
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializer import *

class EmergencyContactViewSet(ModelViewSet):
    serializer_class = EmergencyContactSerializer

    def get_queryset(self):
        queryset = EmergencyContact.objects.select_related('patient__user').all()
        patient_id = self.kwargs.get('patient_pk')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset        

    
    def get_serializer_context(self):
        pateint = self.kwargs.get('patient_pk')
        return {'patient_id':str(pateint)}

     
class VisitViewSet(ModelViewSet):
    serializer_class = VisitsSerializer

    def get_queryset(self):
        queryset = Visits.objects.select_related('patient').select_related('doctor').select_related('nurse').all()
        patient_id = self.kwargs.get('patient_pk')
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
     

