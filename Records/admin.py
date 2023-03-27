from django.contrib import admin
from .models import * 
# Register your models here.
admin.site.register(Visits)
admin.site.register(Vitals)
admin.site.register(EmergencyContact)
admin.site.register(MedicalRecord)
admin.site.register(SurgeryInfo)