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

class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()
    department = DepartmentSerializer()
    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = ['id','user','specialty','medical_license','department','image']

class CreateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user','specialty','medical_license','department','image']

class UpdateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user','specialty','medical_license','department','image']
    specialty = SpecialtySerializer()
    department = DepartmentSerializer()
    user = UpdateUserSerializer


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['user','specialty','medical_license']

class MedicalSecretarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalSecretary
        fields = ['id','user']

class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = ['id','user']



class PatientSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Patient
        fields = ['id','user','address']
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