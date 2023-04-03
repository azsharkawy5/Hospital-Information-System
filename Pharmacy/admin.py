from django.contrib import admin
from .models import *
# Register your models here.


# Compare this snippet from pharmacy\views.py:


admin.site.register(Drug)
admin.site.register(CurrentMedication)
admin.site.register(DrugRequestDetail)
admin.site.register(Pharmacist)
admin.site.register(DispensingDetails)
admin.site.register(Dispensing)

