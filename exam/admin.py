from django.contrib import admin
from exam.models import ClassTest, Midterm, Final, MidRoutine, FinalRoutine

admin.site.register(ClassTest)
admin.site.register(Midterm)
admin.site.register(Final)
admin.site.register(MidRoutine)
admin.site.register(FinalRoutine)