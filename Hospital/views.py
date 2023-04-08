from django.http import Http404
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializer import *
# Create your views here.
def media(request,id):
    media = get_object_or_404(Doctor,pk = id).image
    return render(request, 'media/media.html',{'media' : media})
        
class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.select_related('user').all()
    serializer_class = DoctorSerializer