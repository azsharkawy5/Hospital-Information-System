from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from Core.serializer import UserSerializer,UserCreateSerializer,UpdateUserSerializer
from Core.models import User

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ['name','drug_form','brand_name','stock_level','price']