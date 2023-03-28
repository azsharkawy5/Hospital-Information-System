from django.http import Http404
from django.shortcuts import render
from .models import Doctor
from django.shortcuts import get_object_or_404
# Create your views here.
def media(request,id):
    media = get_object_or_404(Doctor,pk = id).image
    return render(request, 'media/media.html',{'media' : media})
        