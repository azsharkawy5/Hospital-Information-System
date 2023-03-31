from django.contrib import admin
from .models import Exam_Request, Radiolgy_Result, Test_Result, Exam_Details, Examination_list

admin.site.register(Exam_Request)
admin.site.register(Radiolgy_Result)
admin.site.register(Test_Result)
admin.site.register(Examination_list)
admin.site.register(Exam_Details)
