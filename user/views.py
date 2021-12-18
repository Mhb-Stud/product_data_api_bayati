from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from shop.serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User
from .tasks import download_vendor_photo


class UserProductView(viewsets.ViewSet):
    """this class is responsible to send back the user's products in the database knowing that their username is saved
    as a vendor in the database
    """
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        data = VendorProduct.objects.get_vendor_products_by_view(request.user.username)
        return Response(data)


class RegisterView(viewsets.ViewSet):
    """this class does the job for us it takes the user registration form by a post request
    and in json format sends the data to RegisterSerializer"""
    def create(self, request):
        new_user_data = request.data
        User.objects.create_user(username=new_user_data['username'], email=new_user_data['email'],
                                 password=new_user_data['password'], password2=new_user_data['password2'])
        return Response(status=200)


class PhotoUpload(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        download_vendor_photo.delay(request.data['image_url'], request.user.username)
        return Response({"massage": 'the photo will be applied to your profile as soon as possible!'})

