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
router.register('patient',Hospital.views.PatientViewSet,basename='patient')

patient_router = routers.NestedDefaultRouter(router,'patient',lookup ='patient')
patient_router.register('medical-record',views.MedicalRecordViewSet,basename='medicalrecord')
patient_router.register('vitals',views.VitalViewSet,basename='patient-vitals')
patient_router.register('visits',views.VisitViewSet,basename='patient-visits')
patient_router.register('surgery',views.SurgeryViewSet,basename='patient-surgery')
patient_router.register('emergency-contact',views.EmergencyContactViewSet,basename='patient-emergencycontact')

urlpatterns = router.urls + patient_router.urls 