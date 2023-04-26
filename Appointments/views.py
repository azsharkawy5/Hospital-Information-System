from django.shortcuts import render
from .models import *
from Hospital.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework import exceptions



from pprint import pprint

# this is the view for the all  DoctorSchedule
class DoctorScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorScheduleSerializer
    filter_backends = [DjangoFilterBackend] 
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = '__all__'
    pagination_class = pagination.PageNumberPagination
    def get_queryset(self):
        doctor = self.request.query_params.get('doctor', None)
        if doctor is not None:
            queryset = DoctorSchedule.objects.select_related('doctor').filter(doctor=doctor)
            return queryset
        else:
            queryset = DoctorSchedule.objects.select_related('doctor').all()
            return queryset
        


# this is the view for the all  DoctorSlots
class DoctorSlotsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSlotsSerializer
    filter_backends = [DjangoFilterBackend]
    def get_queryset(self):
        date = self.request.query_params.get('date')
        schedule = self.request.query_params.get('schedule')
        doctor = self.request.query_params.get('doctor')
        if date is None or schedule is None or doctor is None:
            raise exceptions.ValidationError({'Error':'Please provide date, schedule and doctor'})
        booked_slots = BookedAppointment.objects.filter(date=date, slot__schedule=schedule, doctor=doctor).values_list('slot__pk', flat=True)
        queryset = Slot.objects.filter(schedule=schedule).exclude(pk__in=booked_slots).select_related('schedule')
        return queryset



class BookedAppoitnmentViewSet(viewsets.ModelViewSet):
    serializer_class = BookedAppoitnmentSerilizer
    queryset = BookedAppointment.objects.all()
    pagination_class = pagination.PageNumberPagination
    sorted_by = ['date']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
