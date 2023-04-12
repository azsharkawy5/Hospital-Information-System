from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *


class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = ['patient','__str__','email','gender','phone','relative_relation']


class SergeryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgeryInfo
        fields = ['patient','doctor','surgery_type','date','time','documentation']


class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = '__all__'

class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = '__all__'

class MedicalRecordSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields =['patient','diagnosis','allergies','family_history','vitals','surgerys']
    vitals = VitalSerializer(Vitals)
    surgerys = SergeryInfoSerializer(SurgeryInfo)
