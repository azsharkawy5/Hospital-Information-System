from django.urls import path
from Core.views import *
from rest_framework_simplejwt.views import TokenObtainPairView 

urlpatterns = [
    path ('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]