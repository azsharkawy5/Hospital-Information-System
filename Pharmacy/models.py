from django.db import models
from django.conf import settings
# Create your models here.


class Drug(models.Model):
    drug_id = models.AutoField(primary_key=True)
    drug_name = models.CharField(max_length=50)
    drug_type = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    drug_price = models.IntegerField()
    drug_quantity = models.IntegerField()
    drug_company = models.CharField(max_length=50)
    drug_description = models.CharField(max_length=100)
    stock_level = models.IntegerField()
    expiry_date = models.DateField()
    


class current_medication(models.Model):
    current_medication_id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    Appointment_id = models.IntegerField()
    time_date = models.DateTimeField()



class DrugReDetails(models.Model):
    Current_medication_id = models.ForeignKey(current_medication, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    amount = models.IntegerField()
    frquency = models.IntegerField()
    duration = models.IntegerField()
    dispense = models.IntegerField()




class Pharmacist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Pharmacist_license = models.IntegerField()




class dispensin(models.Model):
    dispensin_id = models.AutoField(primary_key=True)
    current_medication_id = models.ForeignKey(current_medication, on_delete=models.CASCADE)
    Pharmacist_id = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    time_date = models.DateTimeField()



class dispensin_details(models.Model):
    dispensin_id = models.ForeignKey(dispensin, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)