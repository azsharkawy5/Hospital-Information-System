from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','get_name','specialty','medical_license','department','image']