from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from shop.models import *
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class CrawlerHandler(viewsets.ViewSet):
    """
     for handling the request with a class based view your class should inherit from APIView
     and you should define the get and post method inside your class
    """

    """
    we get the data with objects.all then we send it to serializer to change it from query set into json then we
    send the data back as a response
    """
    def list(self, request):
        data = Product.objects.all()
        serialized = ProductSerializer(data, many=True)
        return Response(serialized.data)

    """ 
    ViewSet class automatically sends post requests to this function here i check weather a vendor sent in json of a 
    product exists in the database if the vendor doesn't exist i add it to the database also we change product type
    using serializer and we send the response back 
    """
    def create(self, request):
        # if DatabaseInterface.should_add_vendor(request.data):
        #     user = User.objects.filter(username=request.data['vendor'])
        #     if user.count() == 1:
        #         ven = Vendor(request.data['vendor'], user[0])
        #     else:
        #         ven = Vendor(request.data['vendor'])
        #     ven.save()

        serialized = ProductSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)


"""
this class is created because i didn't want to write the function in the CrawlerHandler class because it is not related
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


