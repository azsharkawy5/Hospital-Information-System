from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

        
class DoctorViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['department__dapartment_name']
    filterset_fields = ['department__dapartment_name']
    queryset = Doctor.objects.select_related('user').select_related('department').select_related('specialty').all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CreateDoctorSerializer
        return DoctorSerializer

        
    @action(detail=False,methods=['GET','PATCH'],permission_classes=[IsDoctor])
    def me (self,request):
        doctor = Doctor.objects.get(user=request.user)   
        if request.method == 'GET':
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        elif request.method == 'PATCH' :
            serializer =DoctorSerializer(doctor,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        


class NurseViewSet(ModelViewSet):
    queryset = Nurse.objects.select_related('user').all()
    serializer_class = NurseSerializer
    permission_classes = [IsAdminUser]

class PatientViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend,SearchFilter,]
    search_fields = ['user__first_name','user__last_name']
    filterset_fields = ['user__first_name','user__last_name']
    queryset = Patient.objects.select_related('user').select_related('address').all()
    permission_classes = [IsAdminUser]
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CreatePatientSerializer
        elif self.request.method == 'PUT' and self.request.user:
            return UpdatePatientSerializer
        elif self.request.user:
            return PatientSerializer
 
        
    @action(detail=False,methods=['GET','PATCH'],permission_classes=[IsPatient])
    def me (self,request):

        patient = Patient.objects.get(user_id=request.user.id)    
        #patient = Patient.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        elif request.method == 'PATCH' or request.method == 'PUT':
            serializer = UpdatePatientSerializer(patient,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
 


class DepartmentViewSet(ModelViewSet):
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class SpecialtyViewSet(ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class MedicalSecretaryViewSet(ModelViewSet):
    queryset = MedicalSecretary.objects.select_related('user').all()
    serializer_class = MedicalSecretarySerializer
    permission_classes = [IsAdminUser]

    
class ReceptionistViewSet(ModelViewSet):
    queryset = Receptionist.objects.select_related('user').all()
    serializer_class =ReceptionistSerializer 
    permission_classes = [IsAdminUser]
