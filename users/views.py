from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer,LoginSerializer


# Create your views here.

class RegisterView(APIView):
    permission_classes=[]

    def post(self,request):
        serializer=RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user=serializer.save()

        return Response(
            {
                "message": "User Created",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            },
            status=status.HTTP_201_CREATED
        )
    
class LoginView(APIView):
    permission_classes = []

    def post(self,request):

        serializer=LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user=authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        if user is None:
            return Response({
                "message": "Invalid username or password"
            },status=status.HTTP_401_UNAUTHORIZED)

        refresh=RefreshToken.for_user(user)

        return Response({
            "message": "Login successful",
            "Token": str(refresh.access_token),
            "refresh": str(refresh)
        })

class LogoutView(APIView):
    permission_classes=[
        IsAuthenticated
    ]

    def post(self,request):
        refresh_token=request.data.get("refresh")

        if not refresh_token:
            return Response({
                "message":"Refresh token required"
            },status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token=RefreshToken(refresh_token)

            token.blacklist()

            return Response({
                "message": "Logout successful"
            })

        except Exception as e:
            print(e.args)

            return Response({
                "message": "Invalid refresh token"
            },status=status.HTTP_400_BAD_REQUEST)

        