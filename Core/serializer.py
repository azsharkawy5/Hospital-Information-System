from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','gender','phone','national_id','address']