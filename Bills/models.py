from django.db import models

# Create your models here.


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    # patient_id = models.IntegerField()
    time_date = models.DateTimeField()
    # insurance = models.CharField(max_length=50)



class Exam_service(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()


class Medicine_service(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    # curr_med_id = models.IntegerField()



class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    # Appointment_id = models.IntegerField()