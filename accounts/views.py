from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()

class SignupView(APIView):
    # permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            i_am = data['i_am']
            password1 = data['password1']
            password2 = data['password2']
        except KeyError:
            return Response({'error': 'Every field should fillup'})

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email is exists'})
            elif len(password1) < 6:
                return Response({'error': 'Password is too short'})
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, i_am=i_am, password=password1)
                user.save()
                return Response({'success': 'User has been created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})