from django.db import models
from datetime import datetime
from Hospital.models import Doctor


class Exam_Request(models.Model):
    REQUESTED = 'Requested'
    PENDING = 'Pending'
    COMPLETED = 'Completed'

    STATUS = [
        (REQUESTED, 'Requested'),
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS, default=REQUESTED)
    dateTime = models.DateTimeField(default=datetime.now)

    # def __str__(self) -> str:
    #     return self.


class Radiolgy_Result(models.Model):
    Request_id = models.ForeignKey(Exam_Request, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=datetime.now)
    image = models.ImageField(blank=False)
    file = models.FileField(blank=False, default='test')
    comment = models.TextField(max_length=3000, blank=True)


class Test_Result(models.Model):
    Request_id = models.ForeignKey(Exam_Request, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=datetime.now)
    result_value = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    unit = models.CharField(max_length=50, blank=False,  null=True)
    min_reference_range = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    max_reference_range = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    comment = models.TextField(max_length=3000, blank=True, null=True)


class Examination_list(models.Model):
    exam_name = models.CharField(max_length=255, null=True)
    exam_type = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)


class Exam_Details(models.Model):
    exam_id = models.ForeignKey(
        Examination_list, null=False, on_delete=models.PROTECT)
    request_id = models.ForeignKey(
        Exam_Request, null=False, on_delete=models.CASCADE)
