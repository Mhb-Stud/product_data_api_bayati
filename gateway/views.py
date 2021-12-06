from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from shop.models import *
from shop.serializers import *
from rest_framework import viewsets, generics
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
        if 'vendor' in request.data:
            ProcessManager.process(data=request.data, self=ProcessManager())
        else:
            serialized = CategorySerializer(data=request.data)
            if serialized.is_valid():
                Category.objects.process_category(request.data)
                return Response(serialized.data)
            else:
                return Response(serialized.errors)




