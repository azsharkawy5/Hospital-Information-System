from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
