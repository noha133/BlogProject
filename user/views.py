from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from dj_rest_auth.views import (
    LoginView
)
from dj_rest_auth.serializers import JWTSerializerWithExpiration

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    @swagger_auto_schema(
    operation_summary="Register view",
    operation_description="Register view",
    responses={
        201: openapi.Response(description="Created" , schema=JWTSerializerWithExpiration),
    },
    security=[]
    )
    def post(self, request, *args, **kwargs):
        return super().post( request, *args, **kwargs)


class CustomLoginView(LoginView):
    
    @swagger_auto_schema(
    operation_summary="Login view",
    operation_description="Login view",
    responses={
        200: openapi.Response(description="Success" , schema=JWTSerializerWithExpiration),
    },
    security=[]
    )
    def post(self, request, *args, **kwargs):
        return super().post( request, *args, **kwargs)