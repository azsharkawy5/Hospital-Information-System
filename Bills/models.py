from django.db import models
from Appointments.models import BookedAppointment
from Hospital.models import Patient
from Pharmacy.models import CurrentMedication
from Lab_Radiology.models import ExamRequest



# Create your models here.

class InsuranceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='InsuranceDetails')
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
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='Bill')
    time_date = models.DateTimeField()
    insurance = models.ForeignKey(InsuranceDetails, on_delete=models.CASCADE,related_name='Bill')
    


class AppointmentService(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE,related_name='AppointmentService')
    appointment_id = models.ForeignKey(BookedAppointment, on_delete=models.CASCADE,related_name='AppointmentService')

class ExamService(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE,related_name='ExamService')
    exam_request_id = models.ForeignKey(ExamRequest, on_delete=models.CASCADE,related_name='ExamService')



class MedicineService(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE,related_name='MedicineService')
    medication_id = models.ForeignKey(CurrentMedication, on_delete=models.CASCADE,related_name='MedicineService')




