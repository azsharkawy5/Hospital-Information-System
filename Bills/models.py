from django.db import models
from Appointments.models import booked_appointment
from Hospital.models import Patient
from Pharmacy.models import current_medication
from Lab_Radiology.models import Exam_Request



# Create your models here.

class InsuranceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    number = models.IntegerField()
    type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.IntegerField()
    remaining = models.IntegerField()
    status = models.CharField(max_length=50)

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time_date = models.DateTimeField()
    insurance = models.ForeignKey(InsuranceDetails, on_delete=models.CASCADE)
    


class Appointment_service(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    appointment_id = models.ForeignKey(booked_appointment, on_delete=models.CASCADE)

class Exam_service(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    exam_request_id = models.ForeignKey(Exam_Request, on_delete=models.CASCADE)



class Medicine_service(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    current_medicine_id = models.ForeignKey(current_medication, on_delete=models.CASCADE)




