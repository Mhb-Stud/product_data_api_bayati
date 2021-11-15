from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person
from rest_framework import viewsets

# for handling the request with a class based view your class should inherit from APIView
# and you should define the get and post method inside your class


class TestView(viewsets.ViewSet):

    # in the get method it takes the request as a parameter knowing that it's a get request
    # after that we get all person table rows with .object.all() method and into object format
    # now it's time to convert object format into json format for that we use serializer after
    # the data is in jason format now we can return the data with response method

    def list(self, request):
        data = Person.objects.all()
        serialized = PersonSerializer(data, many=True)
        return Response(serialized.data)

    # for the post method we take the request knowing that it's a post request
    # we use the serializer that we created for our Person model to convert json
    # data into object set with calling same method after that we should check if
    # the data received is valid and in the correct format with is valid after we are
    # sure we can write to database with save
    def create(self, request):
        deserialized = PersonSerializer(data=request.data)
        if deserialized.is_valid():
            deserialized.save()
            return Response(deserialized.data)
        else:
            return Response(deserialized.errors)








