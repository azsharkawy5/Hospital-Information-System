from django.contrib import admin
from .models import Drug, current_medication, DrugReDetails, Pharmacist, dispensin, dispensin_details
# Register your models here.


# Compare this snippet from pharmacy\views.py:
admin.site.register(Drug)
admin.site.register(current_medication)
admin.site.register(DrugReDetails)
admin.site.register(Pharmacist)
admin.site.register(dispensin)
admin.site.register(dispensin_details)

