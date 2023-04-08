from django.db import models
from Hospital.models import *
from datetime import datetime
# Create your models here.
days = [
    ('Saturday', 'Saturday'), 
    ('Sunday', 'Sunday'), 
    ('Monday', 'Monday'), 
    ('Tuesday', 'Tuesday'), 
    ('Wednesday', 'Wednesday'), 
    ('Thursday', 'Thursday'), 
    ('Friday', 'Friday')
    ]

appointment_status = [('pend', 'pending'), ('comp', 'completed'), ('canc', 'cancelled')]
Schedule_Status = [('active', 'active'), ('inactive', 'inactive')]

appointment_duration = [(5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45), (50, 50), (55, 55), (60, 60)]
type_of_appointment = [('new', 'new'), ('followup', 'followup')]

class DoctorSchedule(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_schedule')
    day_of_week = models.CharField(max_length=50, choices=days)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.IntegerField(choices=appointment_duration)
    schedule_status = models.CharField(max_length=10, choices=Schedule_Status)
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.doctor.__str__()




class Slot(models.Model):

    schedule = models.ForeignKey(DoctorSchedule, on_delete=models.CASCADE, related_name='slot_schedule')
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()

    



class BookedAppointment(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='patient_appointment')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='doctor_appointment')
    slot = models.ForeignKey(Slot, on_delete=models.PROTECT,related_name='slot_appointment')
    appointment_date = models.DateField()
    appointment_time = models.TimeField(default=datetime.now)
    appointment_type = models.CharField(max_length=10, choices=type_of_appointment)
    status = models.CharField(max_length=5, choices=appointment_status)




