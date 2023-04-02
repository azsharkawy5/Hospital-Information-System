from django.contrib import admin
from .models import *



# Register your models here.
admin.site.register(DoctorSchedule)
admin.site.register(Slot)
admin.site.register(BookedAppointment)

