from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'