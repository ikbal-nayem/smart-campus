from django.contrib import admin
from department.models import Department, Course, Holiday, Calender

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Holiday)
admin.site.register(Calender)
