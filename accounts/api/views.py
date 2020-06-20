from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.db.models.functions import Concat
from django.db.models import Value
from .permissions import (
	IsSuperAdminOrAdmin,
	IsOwnerOrReadOnly,
	IsTeacherOrOwner,
	is_admin
)
from .serializers import (
	ContactInfo,
	UserPersonalInfo,
	TeacherAcademicInfo,
	TeacherDetailsSerializer,
	TeacherDetailsSafeSerializer,
	StudentAcademicInfo,
	StudentDetailsSerializer,
	StudentDetailsSafeSerializer,
	StaffAcademicInfo,
	StaffDetailsSerializer,
	TeacherListSerializer,
	StudentListSerializer,
	StaffListSerializer,
	CurrentUserSerializer
)
User = get_user_model()


class CurrentUserView(APIView):
	def get(self, request, format=None):
		serializer = CurrentUserSerializer(request.user)
		return Response(serializer.data)


class TeacherListAPIView(ModelViewSet):
	queryset = User.objects.filter(i_am='teacher')
	serializer_class = TeacherListSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	lookup_field = 'username'
	lookup_url_kwarg = 'pk'

	def get_queryset(self):
		user = self.request.user
		department = eval(f'user.{user.i_am}info.department')
		if department:
			return super().get_queryset().filter(teacherinfo__department=department)
		return super().get_queryset() if is_admin(user, admin_type='super') else super().get_queryset().filter(id=user.id)

	def get_detail_serializer_class(self, user_object):
		user = self.request.user
		return StudentDetailsSerializer if user.i_am == 'teacher' or user_object==user else StudentDetailsSafeSerializer

	@action(detail=False, methods=['POST'])
	def search(self, request):
		request.data['from'] = 'teacher'
		return searchUser(request, self.get_queryset, self.get_serializer)
	
	@action(detail=True, methods=['POST'], permission_classes=[IsSuperAdminOrAdmin])
	def verify(self, request, pk=None):
		action = request.data.get('action', None)
		return verifyUser(self.get_object(), action)

	@action(detail=True, methods=['GET'])
	def details(self, request, pk=None):
		user_object = self.get_object()
		detail = self.get_detail_serializer_class(user_object)
		serializer = detail(user_object, context={'request': request})
		return Response(serializer.data)

	@action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=UserPersonalInfo, permission_classes=[*permission_classes, IsTeacherOrOwner])
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

	
	
#                               Student

class StudentListAPIView(ModelViewSet):
	queryset = User.objects.filter(i_am='student')
	serializer_class = StudentListSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	lookup_field = 'username'
	lookup_url_kwarg = 'pk'

	def get_queryset(self):
		user = self.request.user
		department = eval(f'user.{user.i_am}info.department')
		if department:
			return super().get_queryset().filter(studentinfo__department=department)
		return super().get_queryset() if is_admin(user, admin_type='super') else super().get_queryset().filter(id=user.id)

	def get_detail_serializer_class(self, user_object):
		user = self.request.user
		return StudentDetailsSerializer if user.i_am == 'teacher' or user_object==user else StudentDetailsSafeSerializer

	@action(detail=False, methods=['POST'])
	def search(self, request):
		request.data['from'] = 'student'
		return searchUser(request, self.get_queryset, self.get_serializer)

	@action(detail=True, methods=['GET'])
	def details(self, request, pk=None):
		user_object = self.get_object()
		detail = self.get_detail_serializer_class(user_object)
		serializer = detail(user_object, context={'request': request})
		return Response(serializer.data)
	
	@action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=UserPersonalInfo, permission_classes=[*permission_classes, IsTeacherOrOwner])
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

	@action(detail=True, methods=['GET', 'PUT', 'PATCH'], serializer_class=ContactInfo, permission_classes=[*permission_classes, IsTeacherOrOwner])
	def phone(self, request, pk=None):
		user_object = self.get_object()
		if request.method == 'GET':
			serializer = self.get_serializer(user_object.phone.all(), many=True)
			return Response(serializer.data)
		else:
			return updatePhoneNumber(user_object, request, self.get_serializer)














#                                       Staff

class StaffListAPIView(ModelViewSet):
	queryset = User.objects.filter(i_am='staff')
	serializer_class = StaffListSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsTeacherOrOwner)
	lookup_field = 'username'
	lookup_url_kwarg = 'pk'

	def get_queryset(self):
		user = self.request.user
		department = eval(f'user.{user.i_am}info.department')
		if department:
			return super().get_queryset().filter(staffinfo__department=department)
		return super().get_queryset() if is_admin(user, admin_type='super') else super().get_queryset().filter(id=user.id)

	@action(detail=False, methods=['POST'])
	def search(self, request):
		request.data['from'] = 'staff'
		return searchUser(request, self.get_queryset, self.get_serializer)
	
	@action(detail=True, methods=['POST'], permission_classes=[IsSuperAdminOrAdmin])
	def verify(self, request, pk=None):
		action = request.data.get('action', None)
		return verifyUser(self.get_object(), action)

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

def searchUser(request, get_queryset, get_serializer):
	department = request.data.get('department', None)
	name = request.data.get('name', None)
	queryset = get_queryset()
	if department:
		if request.data['from'] == 'teacher':
			queryset = queryset.filter(teacherinfo__department=department)
		elif request.data['from'] == 'student':
			batch = request.data.get('batch', None)
			queryset = queryset.filter(studentinfo__department=department, studentinfo__batch=batch) if batch else queryset.filter(studentinfo__department=department)
		elif request.data['from'] == 'staff':
			queryset = queryset.filter(staffinfo__department=department)
	if name:
		fullname = queryset.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
		queryset = fullname.filter(full_name__icontains=name)
	serializer = get_serializer(queryset, many=True)
	return Response(serializer.data)

def verifyUser(obj, action):
	if action:
		if action == 'verify':
			obj.teacherinfo.is_verified = True
			obj.teacherinfo.save()
			return Response({'detail': 'User verified'})
		elif action == 'delete':
			obj.delete()
			return Response({'detail': 'User deleted'})
		else:
			return Response({'error': f"Unknown action '{action}'"})
	else:
		return Response({'error': f'Unknown keyword'})