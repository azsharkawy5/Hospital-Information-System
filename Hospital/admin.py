from django.contrib import admin
from .models import *
from . import models
# Register your models here.
@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['__str__','specialty']

admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Receptionist)
admin.site.register(MedicalSecretary)
admin.site.register(Department)
admin.site.register(Specialty)
