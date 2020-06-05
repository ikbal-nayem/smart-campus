from django.contrib import admin
from .models import UserAccount, UserInfo, Phonebook, StudentInfo, TeacherInfo, StaffInfo

admin.site.register(UserAccount)
admin.site.register(UserInfo)
admin.site.register(Phonebook)
admin.site.register(TeacherInfo)
admin.site.register(StudentInfo)
admin.site.register(StaffInfo)