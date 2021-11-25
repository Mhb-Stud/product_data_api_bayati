from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets


""" 
 for handling the request with a class based view your class should inherit from APIView
 and you should define the get and post method inside your class
"""
class CrawlerHandler(viewsets.ViewSet):
    """
     in the get method it takes the request as a parameter knowing that it's a get request
     after that we get all person table rows with .object.all() method and into object format
     now it's time to convert object format into json format for that we use serializer after
     the data is in jason format now we can return the data with response method
    """
    def list(self, request):
        data = Product.objects.all()
        serialized = ProductSerializer(data, many=True)
        return Response(serialized.data)

    """ 
    for the post method we take the request knowing that it's a post request
     we use the serializer that we created for our Person model to convert json
     data into object set with calling same method after that we should check if
     the data received is valid and in the correct format with is valid after we are
     sure we can write to database with save
     """
    def create(self, request):
        if DatabaseInterface.should_add_vendor(request.data):
            ven = Vendor(request.data['vendor'])
            ven.save()
        # else:
        #     ven = Vendor.objects.get(name=request.data['vendor'])

        serialized = ProductSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)

class DatabaseInterface:
    is_available = None

    @classmethod
    def should_add_vendor(cls, data):
        cls.is_available = Vendor.objects.filter(name=data['vendor'])
        if cls.is_available.count() == 0:
            return True
        else:
            return False


class UserHandler(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ['TokenAuthentication']
    permission_classes = ['IsAuthenticated']

    def list(self, request):
        data = Product.objects.filter(vendor=request.user.username)
        serialized = ProductSerializer(data, many=True)
        return Response(serialized.data)
