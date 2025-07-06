from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from  rest_framework.permissions import IsAuthenticated  
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SingUpSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
# Create your views here.


User = get_user_model()

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SingUpSerializer
    permission_classes = [AllowAny]

