from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    medical_license = models.CharField(max_length=255)
    department = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Hospital/files/media')

    def __str__(self) -> str:
        return str(self.user.first_name+" "+self.user.last_name)
    
    def mediaAdmin(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    mediaAdmin.short_description = 'Image'
    mediaAdmin.allow_tags = True


class Nurse(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    medical_license = models.CharField(max_length=255)
    def __str__(self) -> str:
        return str(self.user.first_name+" "+self.user.last_name)
        
    
class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user.first_name+" "+self.user.last_name)
    
    def name(self):
        return self.__str__()

