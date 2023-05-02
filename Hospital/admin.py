from django.contrib import admin
from .models import *
from . import models
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Receptionist)
admin.site.register(Address)
#admin.site.register(MedicalSecretary)
admin.site.register(Specialty)
admin.site.register(Department)
