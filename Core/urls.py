from . import views
from .models import *
from rest_framework_nested import routers 

router = routers.DefaultRouter()
router.register('user',views.UserViewSet)

urlpatterns = router.urls
