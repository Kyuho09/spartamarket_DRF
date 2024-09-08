from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User
from django.core.validators import validate_email
from .validators import validate_signup


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

        return Response({})