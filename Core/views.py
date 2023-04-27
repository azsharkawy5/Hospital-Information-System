from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.select_related('user_patient').all()
    serializer_class = UserCreateSerializer
