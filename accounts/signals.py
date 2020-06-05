from django.db.models.signals import post_save
from django.dispatch import receiver

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
        print('user created')
        user = UserInfo.objects.create(user=instance)
        if instance.i_am == 'student':
            user.is_verified = True
            user.save()
            StudentInfo.objects.create(user=instance)
        elif instance.i_am == 'teacher':
            TeacherInfo.objects.create(user=instance)
        elif instance.i_am == 'staff':
            StaffInfo.objects.create(user=instance)
