from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ExaminationList)
class ExaminationListAdmin(admin.ModelAdmin):
    list_display = ['exam_name', 'exam_type', 'price']




admin.site.register(ExamRequest)
admin.site.register(TestResult)
admin.site.register(RadiolgyResult)
admin.site.register(ExamDetails)



