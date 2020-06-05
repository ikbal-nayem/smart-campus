from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Holiday, Calender
from exam.models import ClassTest, MidRoutine, FinalRoutine


#                                       holiday in calender
@receiver(post_save, sender=Holiday)
def addHoliday(sender, instance, created, **kwargs):
    if created:
        Calender.objects.create(event_type='Holiday', date=instance.date, event_id=instance.id)

@receiver(post_delete, sender=Holiday)
def deleteHoliday(sender, instance, **kwargs):
    Calender.objects.get(event_type='Holiday', event_id=instance.id).delete()


#                                       class test in calender
@receiver(post_save, sender=ClassTest)
def addClassTest(sender, instance, created, **kwargs):
    if created:
        Calender.objects.create(event_type='ClassTest', date=instance.date, event_id=instance.code)

@receiver(post_delete, sender=ClassTest)
def deleteClassTest(sender, instance, **kwargs):
    Calender.objects.get(event_type='ClassTest', event_id=instance.code).delete()


#                                           midterm exam in calender
@receiver(post_save, sender=MidRoutine)
def addMidterm(sender, instance, created, **kwargs):
    if created:
        Calender.objects.create(event_type='MidRoutine', date=instance.date, event_id=instance.id)

@receiver(post_delete, sender=MidRoutine)
def deleteMidterm(sender, instance, **kwargs):
    Calender.objects.get(event_type='MidRoutine', event_id=instance.id).delete()


#                                           final exam in calender
@receiver(post_save, sender=FinalRoutine)
def addFinal(sender, instance, created, **kwargs):
    if created:
        Calender.objects.create(event_type='FinalRoutine', date=instance.date, event_id=instance.id)

@receiver(post_delete, sender=FinalRoutine)
def deleteFinal(sender, instance, **kwargs):
    Calender.objects.get(event_type='FinalRoutine', event_id=instance.id).delete()
