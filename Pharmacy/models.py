from django.db import models
from django.conf import settings
from Hospital.models import Patient
# Create your models here.


class Drug(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    drug_form = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    price = models.IntegerField()
    company = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    stock_level = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.brand_name
    

class CurrentMedication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Appointment_id = models.IntegerField()
    time_date = models.DateTimeField()



class DrugReDetail(models.Model):
    medication_id = models.ForeignKey(CurrentMedication, on_delete=models.CASCADE,related_name='DrugReDetail')
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    amount = models.IntegerField()
    frquency = models.IntegerField()
    duration = models.IntegerField()
    dispense = models.IntegerField()




class Pharmacist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Pharmacist_license = models.IntegerField()




class Dispensing(models.Model):
    dispensin_id = models.AutoField(primary_key=True)
    medication_id = models.ForeignKey(CurrentMedication, on_delete=models.CASCADE)
    Pharmacist_id = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    time_date = models.DateTimeField()



class DispensingDetails(models.Model):
    dispensin_id = models.ForeignKey(Dispensing, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)