from django.contrib import admin
from .models import UserAccount, UserInfo, Phonebook, StudentInfo, TeacherInfo, StaffInfo, Administrator


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'username', 'i_am', 'email', 'is_active', )
    list_display_links = ('id', 'get_full_name', 'username')
    list_filter = ('i_am', 'is_superuser', 'teacherinfo__department', 'studentinfo__department', 'staffinfo__department')
    empty_value_display = '-'
    search_fields = ['first_name', 'last_name']


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'get_account_type', '_account_created', )
    list_display_links = ('pk', '__str__')
    list_filter = ('user__i_am', 'user__teacherinfo__department', 'user__studentinfo__department', 'user__staffinfo__department')
    empty_value_display = '-'
    search_fields = ['user__first_name', 'user__last_name']
    def get_account_type(self, obj):
        return obj.user.i_am
    get_account_type.short_description = 'User type'

class PhonebookAdmin(admin.ModelAdmin):
    list_display = ('number', '__str__', 'verified', )
    list_filter = ('user__i_am',)
    empty_value_display = '-'
    search_fields = ['user__first_name', 'user__last_name']

class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'teacher_id',  'department', 'designation', 'is_verified')
    list_display_links = ('pk', '__str__')
    list_filter = ('department', )
    empty_value_display = '-'
    search_fields = ['user__first_name', 'user__last_name', 'designation']

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'student_id', 'department', 'batch')
    list_display_links = ('pk', '__str__')
    list_filter = ('department',)
    empty_value_display = '-'
    search_fields = ['user__first_name', 'user__last_name']

class StaffInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'department',  'designation', 'is_verified')
    list_display_links = ('pk', '__str__')
    list_filter = ('department',)
    empty_value_display = '-'
    search_fields = ['user__first_name', 'user__last_name', 'designation']

class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__',  'administrator_type', 'department')
    list_filter = ('department', 'administrator_type')
    list_display_links = ('pk', '__str__')


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Phonebook, PhonebookAdmin)
admin.site.register(TeacherInfo, TeacherInfoAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(StaffInfo, StaffInfoAdmin)
admin.site.register(Administrator, AdministratorAdmin)