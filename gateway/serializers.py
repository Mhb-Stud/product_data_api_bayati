from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProductSerializer(serializers.ModelSerializer):
    """
     this is a simple product serializer for conversion between json and dictionaries into query sets
     and vice versa
    """
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'base_price', 'vendor']


class VendorSerializer(serializers.ModelSerializer):
    """just a serializer"""
    class Meta:
        model = Vendor
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    """just a serializer"""
    class Meta:
        model = User
        fields = ['username', 'password', 'vendor']

