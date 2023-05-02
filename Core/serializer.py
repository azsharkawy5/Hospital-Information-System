from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name','phone_1','phone_2','gender','national_id'] 

class UserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','phone_1','phone_2','email','gender','national_id']
    
class UpdateUserSerializer(serializers.ModelSerializer):
    # username=serializers.CharField(read_only=True)
    # email=serializers.EmailField(read_only=True)
    # national_id=serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','phone_1','phone_2','email','gender']