from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

class Department(models.Model):
    name = models.CharField(max_length=255)

        
class Specialty(models.Model):
    name = models.CharField(max_length=255)

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty,on_delete=models.CASCADE)
    medical_license = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Hospital/files/media')
    
    def mediaAdmin(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    mediaAdmin.short_description = 'Image'
    mediaAdmin.allow_tags = True


class Nurse(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    medical_license = models.CharField(max_length=255)

    
class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    

class Receptionist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    

class MedicalSecretary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
       