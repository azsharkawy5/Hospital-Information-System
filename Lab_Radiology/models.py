from django.db import models
from datetime import datetime
from Hospital.models import Patient, Doctor


class ExamRequest(models.Model):
    REQUESTED = 'Requested'
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    STATUS = [
        (REQUESTED, 'Requested'),
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]
    request_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS, default=REQUESTED)
    dateTime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.request_id)

class RadiolgyResult(models.Model):
    Request_id = models.ForeignKey(ExamRequest, on_delete=models.CASCADE,related_name='RadiologyRequest')
    dateTime = models.DateTimeField(default=datetime.now)
    image = models.ImageField(blank=False)
    file = models.FileField(blank=False, default='test')
    comment = models.TextField(max_length=3000, blank=True)


class TestResult(models.Model):
    Request_id = models.ForeignKey(ExamRequest, on_delete=models.CASCADE, related_name='TestResult')
    dateTime = models.DateTimeField(default=datetime.now)
    result_value = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    unit = models.CharField(max_length=50, blank=False,  null=True)
    min_reference_range = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    max_reference_range = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    comment = models.TextField(max_length=3000, blank=True, null=True)


class ExaminationList(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)


class ExamDetails(models.Model):
    exam_id = models.ForeignKey(
        ExaminationList, null=False, on_delete=models.PROTECT, related_name='ExamDetails')
    request_id = models.ForeignKey(
        ExamRequest, null=False, on_delete=models.CASCADE, related_name='ExamDetails')
