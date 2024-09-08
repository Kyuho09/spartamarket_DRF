from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        nickname = request.data.get("nickname")
        birth = request.data.get("birth")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")

        user = User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname,
            birth=birth,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        print(user)

        return Response({})