import Hospital
from . import views
from .models import *
from rest_framework_nested import routers 


router = routers.DefaultRouter()
router.register('emergency-contact',views.EmergencyContactViewSet,basename='emergencycontact')
router.register('surgery',views.SurgeryViewSet,basename='surgeryinfo')
router.register('visits',views.VisitViewSet,basename='visits')
router.register('vitals',views.VitalViewSet,basename='vitals')
router.register('medical-record',views.MedicalRecordViewSet,basename='medicalrecord')
router.register('all-records',views.PatientRecordsViewSet,basename='all-records')


urlpatterns = router.urls 