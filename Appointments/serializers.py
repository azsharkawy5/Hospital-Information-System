from rest_framework import serializers
from Hospital.models import Doctor, Specialty
from .models import *


class DoctorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        fields = '__all__'


    

class DoctorSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id','start_time','end_time','schedule']



class BookedAppoitnmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = BookedAppointment
        fields = ['id','patient','doctor','slot','date','type','status']