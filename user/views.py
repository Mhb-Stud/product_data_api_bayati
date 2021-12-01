from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from shop.serializers import *
from .models import *
from rest_framework import viewsets, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserHandler(viewsets.ViewSet):
    """
    this class is responsible to send back the user's products in the database knowing that their username is saved as a
    vendor in the database
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        data = Product.objects.filter(vendor=request.user.username)
        serialized = ProductSerializer(data, many=True)
        return Response(serialized.data)


class RegisterView(generics.CreateAPIView):
    """
    this is a generic class for handling user registration since we don't need to do anything special this class does the
    job for us it takes the user registration form by a post request and in json format sends the data to RegisterSerializer
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
