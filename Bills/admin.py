from django.contrib import admin
from .models import Bill, ExamService, MedicineService

# Register your models here.

admin.site.register(Bill)
admin.site.register(ExamService)
admin.site.register(MedicineService)

