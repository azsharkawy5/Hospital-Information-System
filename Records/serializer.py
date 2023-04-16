from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from Hospital.serializer import *


class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = ['id','first_name','last_name','email','gender','phone','relative_relation']

    def create(self, validated_data):
            patient_id =self.context['patient_id']
            return EmergencyContact.objects.create(patient_id=patient_id,**validated_data)

class SergeryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgeryInfo
        fields = ['id','doctor','surgery_type','date','time','documentation']

    def create(self, validated_data):
            patient_id =self.context['patient_id']
            return SurgeryInfo.objects.create(patient_id=patient_id,**validated_data)


class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = ['id','doctor','nurse','room_number','bed_number','admission_date','discharge_date','diagnosis','notes']
    
    def create(self, validated_data):
        patient_id =self.context['patient_id']
        return Visits.objects.create(patient_id=patient_id,**validated_data)
    


    
class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = ['id','date','time','height','weight','blood_pressure','heart_rate','temperature']

    def create(self, validated_data):
        patient_id =self.context['patient_id']
        return Vitals.objects.create(patient_id=patient_id,**validated_data)
   

class MedicalRecordSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields =['diagnosis','allergies','family_history']

    def create(self, validated_data):
        patient_id =self.context['patient_id']
        return MedicalRecord.objects.create(patient_id=patient_id,**validated_data)

class PatientAllRecordrSerializer(serializers.ModelSerializer):
    medical_record = serializers.SerializerMethodField()
    vitals = serializers.SerializerMethodField()
    surgeries = serializers.SerializerMethodField()
    visits = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['name','medical_record','vitals','visits','surgeries']
    
    def get_vitals(self,obj):
        vitals = obj.patient_vital.all()
        return VitalSerializer(vitals,many=True).data
    
    def get_visits(self,obj):
        visits = obj.inpatient.all()
        return VisitsSerializer(visits,many=True).data
    
    def get_surgeries(self,obj):
        surgeries = obj.patient_surgery.all()
        return SergeryInfoSerializer(surgeries,many=True).data
    
    def get_medical_record(self,obj):
        medical_record = obj.patient_record
        return MedicalRecordSerializer(medical_record).data
    
   
 