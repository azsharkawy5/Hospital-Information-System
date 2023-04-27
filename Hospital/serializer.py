from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from Core.serializer import UserSerializer,UserCreateSerializer,UpdateUserSerializer
from Core.models import User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['apartment_number','street','city','country']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','dapartment_name']

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id','specialty']    

class DoctorSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user','specialty','medical_license','department','image']
    specialty = SpecialtySerializer()
    department = DepartmentSerializer()
    #user = UserSerializer(read_only =1)


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['user','specialty','medical_license']
    #user = UserSerializer(User)


class PatientSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Patient
        fields = ['user','id','address']
    user = UserSerializer()

class CreatePatientSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Patient
        fields = ['user','id','address']
    #user = UserCreateSerializer()

class UpdatePatientSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Patient
        fields = ['user','id','address']
    user = UpdateUserSerializer()