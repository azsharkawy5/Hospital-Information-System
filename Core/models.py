from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    genders = [
        ('M','Male'),
        ('F','Female'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique= 1)
    gender = models.CharField(max_length=1,choices=genders)
    phone = PhoneNumberField()
    national_id = models.CharField(max_length=14,unique=1)
    address = models.CharField(max_length=300)
    
 
    
