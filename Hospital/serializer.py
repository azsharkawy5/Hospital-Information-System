from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from Core.serializer import UserSerializer
from Core.models import User

class DoctorSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user','specialty','medical_license','department','image']
    #user = UserSerializer(read_only =1)


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['user','specialty','medical_license']
    #user = UserSerializer(User)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['user',]
    #user = UserSerializer(User)