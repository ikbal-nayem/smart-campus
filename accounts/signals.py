from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import (
    UserAccount,
    UserInfo,
    StudentInfo,
    TeacherInfo,
    StaffInfo
)

@receiver(post_save, sender=UserAccount)
def NewUserCreated(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserInfo.objects.create(user=instance)
        if instance.i_am == 'student':
            StudentInfo.objects.create(user=instance)
        elif instance.i_am == 'teacher':
            TeacherInfo.objects.create(user=instance)
        elif instance.i_am == 'staff':
            StaffInfo.objects.create(user=instance)
