from . import views
from .models import *
from rest_framework_nested import routers 
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('doctor',views.DoctorViewSet)
router.register('nurse',views.NurseViewSet)
router.register('patient',views.PatientViewSet)
router.register('medical-secretary',views.MedicalSecretaryViewSet)
router.register('receptionist',views.ReceptionistViewSet)
router.register('address',views.AddressViewSet)
router.register('department',views.DepartmentViewSet)
router.register('specialty',views.SpecialtyViewSet)

urlpatterns= router.urls