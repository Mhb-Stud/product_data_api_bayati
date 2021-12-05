from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from shop.models import *
from shop.serializers import *
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from shop.managers import *


class CrawlerHandler(viewsets.ViewSet):
    """for handling the request with a class based view your class should inherit from APIView
     and you should define the get and post method inside your class
    """

    def list(self, request):
        """we get the data with objects.all then we send it to serializer to change it from query set into json then we
        send the data back as a response
        """
        data = Product.objects.all()
        serialized = ProductSerializer(data, many=True)
        return Response(serialized.data)

    def create(self, request):
        """ViewSet class automatically sends post requests to this function here i redirect to managers.py"""
        # if DatabaseInterface.should_add_vendor(request.data):
        #     user = User.objects.filter(username=request.data['vendor'])
        #     if user.count() == 1:
        #         ven = Vendor(request.data['vendor'], user[0])
        #     else:
        #         ven = Vendor(request.data['vendor'])
        #     ven.save()
        if 'vendor' is request.data:
            Manager.process(request.data)
        else:
            serialized = CategorySerializer(data=request.data)
            if serialized.is_valid():
                Category.objects.process_category(request.data)
                return Response(serialized.data)
            else:
                return Response(serialized.errors)


"""this class is created because i didn't want to write the function in the CrawlerHandler class because it is not related
to that class and its related to our database
"""

class DatabaseInterface:
    is_available = None

    @classmethod
    def should_add_vendor(cls, data):
        cls.is_available = Vendor.objects.filter(name=data['vendor'])
        if cls.is_available.count() == 0:
            return True
        else:
            return False


