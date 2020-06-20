import random
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            i_am = data['i_am']
            password1 = data['password1']
            password2 = data['password2']
        except Exception as e:
            return Response({'error': f'{str(e).strip()} field is require'})

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            elif len(password1) < 6:
                return Response({'error': 'Password is too short'})
            else:
                username = makeUsername(first_name, last_name)
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, i_am=i_am, password=password1)
                user.save()
                token = Token.objects.get(user=user).key
                return Response({'success': 'User has been created successfully', 'token': token})
        else:
            return Response({'error': 'Password do not match'})

def makeUsername(first_name, last_name):
    full_name = (first_name+last_name).replace(' ', '').lower()
    if len(full_name)<=10:
        name = full_name
        while User.objects.filter(username=name).exists():
            name = full_name+str(random.choice(range(999)))
        return name

    first_name = first_name.replace(' ', '').lower()
    if len(first_name)<=10:
        name = first_name
        while User.objects.filter(username=name).exists():
            name = first_name+str(random.choice(range(999)))
        return name

    last_name = last_name.replace(' ', '').lower()
    name = last_name
    while User.objects.filter(username=name).exists():
        name = last_name+str(random.choice(range(999)))
    return name