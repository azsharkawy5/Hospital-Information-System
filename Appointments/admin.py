from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'day_of_week', 'start_time', 'end_time', 'slot_duration', 'schedule_status', 'price']

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ['__str__','get_day' ,'start_time', 'end_time']


@admin.register(BookedAppointment)
class BookedAppointmentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'patient', 'doctor', 'slot', 'date', 'type']

