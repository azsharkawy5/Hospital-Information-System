from django.db import models
from django.conf import settings
from Hospital.models import Patient,Doctor
from Appointments.models import BookedAppointment
from datetime import datetime
# Create your models here.


class Drug(models.Model):

    name = models.CharField(max_length=50)
    drug_form = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    stock_level = models.PositiveIntegerField(default=0)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name + ' ' + self.brand_name
    

class CurrentMedication(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='patient_medication')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='doctor_request')
    appointment = models.ForeignKey(BookedAppointment, on_delete=models.CASCADE,related_name='appointment')



class DrugRequestDetail(models.Model):

    medication = models.ForeignKey(CurrentMedication, on_delete=models.CASCADE,related_name='medication_detail')
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE,related_name='drug_detail')
    frquency = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    dispense = models.BooleanField(default=False)




class Pharmacist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Pharmacist_license = models.CharField(max_length=50)




class Dispensing(models.Model):

    medication = models.ForeignKey(CurrentMedication, on_delete=models.CASCADE,related_name='medication_dispense')
    Pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE,related_name='dispenser')
    time_date = models.DateTimeField()



class DispensingDetails(models.Model):
    dispensing = models.ForeignKey(Dispensing, on_delete=models.CASCADE,related_name='dispensing_detail')
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE,related_name='drug_dispense')