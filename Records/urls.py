import Hospital
from . import views
from .models import *
from rest_framework_nested import routers 


router = routers.DefaultRouter()
router.register('emergency-contact',views.EmergencyContactViewSet)
router.register('surgery',views.SurgeryViewSet)
router.register('visits',views.VisitViewSet)
router.register('vitals',views.VitalViewSet)
router.register('medical-record',views.MedicalRecordViewSet)
router.register('patient',Hospital.views.PatientViewSet)

patient_router = routers.NestedDefaultRouter(router,'patient',lookup ='patient')
patient_router.register('medical-record',views.MedicalRecordViewSet,basename='patient-medicalrecord')
patient_router.register('vitals',views.VitalViewSet,basename='patient-vitals')
patient_router.register('visits',views.VisitViewSet,basename='patient-visits')
patient_router.register('surgery',views.SurgeryViewSet,basename='patient-surgery')
patient_router.register('emergency-contact',views.EmergencyContactViewSet,basename='patient-emergencycontact')
urlpatterns = router.urls + patient_router.urls 