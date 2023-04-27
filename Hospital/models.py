from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

class Department(models.Model):
    dapartment_name = models.CharField(max_length=100)

class Specialty(models.Model):
    specialty = models.CharField(max_length=100)

class Address(models.Model):
    apartment_number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_doctor')
    specialty = models.ForeignKey(Specialty,related_name='doctor_specialty',on_delete=models.CASCADE)
    medical_license = models.CharField(max_length=255)
    department = models.ForeignKey(Department,related_name='doctor_department',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Hospital/files/media')

    def __str__(self) -> str:
        return str(self.user.first_name+" "+self.user.last_name)
    
    def mediaAdmin(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    mediaAdmin.short_description = 'Image'
    mediaAdmin.allow_tags = True


class Nurse(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_nurse')
    specialty = models.CharField(max_length=255)
    medical_license = models.CharField(max_length=255)
    def __str__(self) -> str:
        return str(self.user.first_name+" "+self.user.last_name)
        
    
class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_patient')
    address = models.ForeignKey(Address,related_name='patient_address',on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user.first_name+" "+self.user.last_name)
    
    def name(self):
        return self.__str__()
    
class Receptionist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user.first_name+" "+self.user.last_name)
