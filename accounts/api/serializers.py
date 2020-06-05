from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField
)
from django.contrib.auth import get_user_model
from department.models import Course
from ..models import (
    UserInfo,
    Phonebook,
    TeacherInfo,
    StaffInfo,
    StudentInfo
)
User = get_user_model()


class UserPersonalInfo(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            'father_name', 'mother_name', 'gender', 'birth_date',
            'religion', 'blood_group', 'present_address', 'permanent_address',
            'facebook_url', 'picture',
            '_account_created', '_account_updated'
        ]
        read_only_fields = ['_account_created', '_account_updated']

class ContactInfo(ModelSerializer):
    class Meta:
        model = Phonebook
        fields = ['id', 'number', 'verified']
        read_only_fields = ['id']
    


#                                           teacher serializer
class CourseTakes(ModelSerializer):
    class Meta:
        model = Course
        fields = ['code', 'name']
        read_only_fields = ['code']

class TeacherAcademicInfo(ModelSerializer):
    course_info = CourseTakes(many=True, required=False, read_only=True)
    course_takes = PrimaryKeyRelatedField(many=True, required=False, read_only=True)
    class Meta:
        model = TeacherInfo
        fields = [
            'teacher_id', 'is_verified', 'department', 'designation',
            'degree', 'marital_status', 'joining_date',
            'course_takes', 'course_info'
        ]
    def update(self, instance, validated_data):
        if validated_data.get('course_list'):
            course_list = validated_data.pop('course_list')
            previous_list = [c.code for c in instance.course_takes.all()]
            for course in course_list:
                try:
                    previous_list.pop(previous_list.index(course))
                except ValueError:
                    pass
                instance.course_takes.add(Course.objects.get(code=course))
            for pre in previous_list:
                instance.course_takes.remove(Course.objects.get(code=pre))
        return super().update(instance, validated_data)


class TeacherDetailsSerializer(ModelSerializer):
    picture = SerializerMethodField('get_picture_url')
    userinfo = UserPersonalInfo(many=False)
    phone = ContactInfo(many=True)
    academic_info = TeacherAcademicInfo(many=False)
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'is_active',
            'userinfo', 'picture', 'academic_info', 'phone'
        ]

    def get_picture_url(self, user):
        return self.context['request'].build_absolute_uri(user.userinfo.picture.url)

class TeacherListSerializer(ModelSerializer):
    profile_picture = SerializerMethodField('get_picture_url')
    department = SerializerMethodField('get_department')
    designation = SerializerMethodField('get_designation')
    is_verified = SerializerMethodField('get_is_verified')
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'i_am', 'department', 'designation', 'is_active', 'profile_picture', 'is_verified']

    def get_picture_url(self, user):
        return self.context['request'].build_absolute_uri(user.userinfo.picture.url)
    def get_department(self, user):
        return user.teacherinfo.department.code if user.teacherinfo.department else None
    def get_designation(self, user):
        return user.teacherinfo.designation
    def get_is_verified(self, user):
        return user.teacherinfo.is_verified


#                                           student serializer
class StudentAcademicInfo(ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = [
            'student_id', 'department', 'batch',
            'section', 'session', 'registration',
            'addmission_date'
        ]

class StudentDetailsSerializer(ModelSerializer):
    picture = SerializerMethodField('get_picture_url')
    userinfo = UserPersonalInfo(many=False)
    phone = ContactInfo(many=True)
    academic_info = StudentAcademicInfo(many=False)
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'is_active',
            'userinfo', 'picture', 'academic_info', 'phone'
        ]

    def get_picture_url(self, user):
        return self.context['request'].build_absolute_uri(user.userinfo.picture.url)


class StudentListSerializer(ModelSerializer):
    profile_picture = SerializerMethodField('get_picture_url')
    student_id = SerializerMethodField('get_student_id')
    department = SerializerMethodField('get_department')
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'i_am', 'department', 'student_id', 'is_active', 'profile_picture']
    
    def get_picture_url(self, user):
        return self.context['request'].build_absolute_uri(user.userinfo.picture.url)
    def get_student_id(self, user):
        return user.studentinfo.student_id
    def get_department(self, user):
        return user.studentinfo.department.code if user.studentinfo.department else None


#                                            staff serializer
class StaffAcademicInfo(ModelSerializer):
    class Meta:
        model = StaffInfo
        fields = [
            'is_verified', 'department', 'designation',
            'qualifications', 'marital_status',
            'joining_date'
        ]

class StaffDetailsSerializer(ModelSerializer):
    picture = SerializerMethodField('get_picture_url')
    userinfo = UserPersonalInfo(many=False)
    phone = ContactInfo(many=True)
    academic_info = StaffAcademicInfo(many=False)
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'is_active',
            'userinfo', 'picture', 'academic_info', 'phone'
        ]

    def get_picture_url(self, user):
        return self.context['request'].build_absolute_uri(user.userinfo.picture.url)


class StaffListSerializer(ModelSerializer):
    profile_picture = SerializerMethodField('get_picture_url')
    designation = SerializerMethodField('get_designation')
    department = SerializerMethodField('get_department')
    is_verified = SerializerMethodField('get_is_verified')
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'i_am', 'designation', 'department', 'is_active', 'profile_picture', 'is_verified']

    def get_picture_url(self, user):
        return self.context['request'].build_absolute_uri(user.userinfo.picture.url)
    def get_designation(self, user):
        return user.staffinfo.designation
    def get_department(self, user):
        return user.staffinfo.department.code if user.staffinfo.department else None
    def get_is_verified(self, user):
        return user.staffinfo.is_verified
