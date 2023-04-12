from . import views
from .models import *
from rest_framework_nested import routers 

router = routers.DefaultRouter()
router.register('emergencycontact',views.EmergencyContactViewSet)
router.register('surgery',views.SurgeryViewSet)
router.register('visits',views.VisitViewSet)
router.register('vitals',views.VitalViewSet)
router.register('medicalrecord',views.MedicalRecordViewSet)

urlpatterns = router.urls