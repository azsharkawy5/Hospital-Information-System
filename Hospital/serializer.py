from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user','get_name','specialty','medical_license','department','image']


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['user','__str__','specialty','medical_license']