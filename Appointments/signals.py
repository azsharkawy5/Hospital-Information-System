from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from  datetime import timedelta
import pprint
def converter(time):
    hours = int(time[0] + time[1])
    minutes = int(time[3] + time[4])
    new_time = timedelta(minutes=minutes,hours=hours)
    return new_time

@receiver(post_save, sender=DoctorSchedule)
def create_slots(sender, instance,created, **kwargs):
    pprint.pprint("Hello1")
    if created:
        pprint.pprint("Hello2")
        i = instance
        start = converter(str(i.start_time))
        pprint.pprint("Hello3")
        end = start
        while start < converter(str(i.end_time)):
            pprint.pprint("Hello4")
            end = start + timedelta(minutes=i.slot_duration) 
            Slot.objects.create(schedule_id=i.pk, start_time=str(start), end_time=str(end))
            pprint.pprint("Hello5")
            start = end


@receiver(post_delete, sender=DoctorSchedule)
def delete_slots(sender, instance, **kwargs):
    Slot.objects.filter(schedule_id=instance.pk).delete()     