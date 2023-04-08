from . import views
from .models import *
from rest_framework_nested import routers 
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('doctor',views.DoctorViewSet)
router.register('nurse',views.NurseViewSet)
router.register('patient',views.PatientViewSet)

urlpatterns= router.urls