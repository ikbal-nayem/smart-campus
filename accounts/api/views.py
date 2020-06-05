from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .serializers import (
    ContactInfo,
    UserPersonalInfo,
    TeacherAcademicInfo,
    TeacherDetailsSerializer,
    StudentAcademicInfo,
    StudentDetailsSerializer,
    StaffAcademicInfo,
    StaffDetailsSerializer,
    TeacherListSerializer,
    StudentListSerializer,
    StaffListSerializer
)

User = get_user_model()

class TeacherListAPIView(ModelViewSet):
    queryset = User.objects.filter(i_am='teacher')
    serializer_class = TeacherListSerializer

    @action(detail=True, methods=['GET'], serializer_class=TeacherDetailsSerializer)
    def details(self, request, pk=None):
        user_object = self.get_object()
        serializer = self.get_serializer(user_object, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=UserPersonalInfo)
    def userinfo(self, request, pk=None):
        user_object = self.get_object().userinfo
        return updateUserInfo(user_object, request, self.get_serializer)

    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=TeacherAcademicInfo)
    def academic_info(self, request, pk=None):
        user_object = self.get_object().teacherinfo
        if request.method == 'GET':
            serializer = self.get_serializer(user_object, context={'request': request})
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(user_object, data=request.data)
            course_list = serializer.initial_data.pop('course_takes') if serializer.initial_data.get('course_takes') else []
            if serializer.is_valid():
                serializer.validated_data['course_list'] = course_list
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    
    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=ContactInfo)
    def phone(self, request, pk=None):
        user_object = self.get_object()
        if request.method == 'GET':
            serializer = self.get_serializer(user_object.phone.all(), many=True)
            return Response(serializer.data)
        else:
            return updatePhoneNumber(user_object, request, self.get_serializer)

    
    

class StudentListAPIView(ModelViewSet):
    queryset = User.objects.filter(i_am='student')
    serializer_class = StudentListSerializer

    @action(detail=True, methods=['GET'], serializer_class=StudentDetailsSerializer)
    def details(self, request, pk=None):
        user_object = self.get_object()
        serializer = self.get_serializer(user_object, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=UserPersonalInfo)
    def userinfo(self, request, pk=None):
        user_object = self.get_object().userinfo
        return updateUserInfo(user_object, request, self.get_serializer)
    
    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=StudentAcademicInfo)
    def academic_info(self, request, pk=None):
        user_object = self.get_object().studentinfo
        if request.method == 'GET':
            serializer = self.get_serializer(user_object)
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(user_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=ContactInfo)
    def phone(self, request, pk=None):
        user_object = self.get_object()
        if request.method == 'GET':
            serializer = self.get_serializer(user_object.phone.all(), many=True)
            return Response(serializer.data)
        else:
            return updatePhoneNumber(user_object, request, self.get_serializer)




class StaffListAPIView(ModelViewSet):
    queryset = User.objects.filter(i_am='staff')
    serializer_class = StaffListSerializer

    @action(detail=True, methods=['GET'], serializer_class=StaffDetailsSerializer)
    def details(self, request, pk=None):
        user_object = self.get_object()
        serializer = self.get_serializer(user_object, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=UserPersonalInfo)
    def userinfo(self, request, pk=None):
        user_object = self.get_object().userinfo
        return updateUserInfo(user_object, request, self.get_serializer)

    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=StaffAcademicInfo)
    def academic_info(self, request, pk=None):
        user_object = self.get_object().staffinfo
        if request.method == 'GET':
            serializer = self.get_serializer(user_object)
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(user_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    @action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=ContactInfo)
    def phone(self, request, pk=None):
        user_object = self.get_object()
        if request.method == 'GET':
            serializer = self.get_serializer(user_object.phone.all(), many=True)
            return Response(serializer.data)
        else:
            return updatePhoneNumber(user_object, request, self.get_serializer)



def updateUserInfo(user_object, request, get_serializer):
    if request.method == 'GET':
        serializer = get_serializer(user_object)
        return Response(serializer.data)
    else:
        serializer = get_serializer(user_object, data=request.data)
        if serializer.is_valid():
            updateUser(user_object, serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

def updateUser(user_object, serializer):
    first_name = serializer.initial_data.get('first_name', user_object.user.first_name)
    last_name = serializer.initial_data.get('last_name', user_object.user.last_name)
    email = serializer.initial_data.get('email', user_object.user.email)
    user = User.objects.get(id = user_object.pk)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()

def updatePhoneNumber(user_object, request, get_serializer):
    pre_number_list = [ph.number for ph in user_object.phone.all()]
    try:
        new_list = request.data['numbers']
        if type(new_list) is not list:
            return Response({'error': 'numbers should be a list of phone number'})
    except KeyError:
        return Response({'error': 'numbers field is required'})
    for number in pre_number_list:
        if number not in new_list:
            user_object.phone.get(number=number).delete()
    for number in new_list:
        if number not in pre_number_list:
            user_object.phone.create(number=number)
    serializer = get_serializer(user_object.phone.all(), many=True)
    return Response(serializer.data)