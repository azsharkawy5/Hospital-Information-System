from django.contrib import admin
from .models import Bill, Exam_service, Medicine_service, Appointment

# Register your models here.

admin.site.register(Bill)
admin.site.register(Exam_service)
admin.site.register(Medicine_service)
admin.site.register(Appointment)
