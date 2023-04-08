from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ExaminationList)
admin.site.register(ExamRequest)
admin.site.register(TestResult)
admin.site.register(RadiolgyResult)
admin.site.register(ExamDetails)



