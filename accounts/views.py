from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User
from django.core.validators import validate_email
from .validators import validate_signup
from .serializers import UserSerializer
from django.contrib.auth import authenticate


# Create your views here.
class SignupView(APIView):
    def post(self, request):
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=400)

        user = User.objects.create_user(
            username = request.data.get("username"),
            password = request.data.get("password"),
            nickname = request.data.get("nickname"),
            birth = request.data.get("birth"),
            first_name = request.data.get("first_name"),
            last_name = request.data.get("last_name"),
            email = request.data.get("email"),
        )

        serializer = UserSerializer(user)
        return Response(serializer.data)


class SigninView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "아이디 혹은 비밀번호가 올바르지 않습니다."}, status=400
            )

        serializer = UserSerializer(user)
        res_data = serializer.data
        res_data["access_token"] = "123123"
        res_data["refresh_token"] = "4545454"
        return Response(res_data)