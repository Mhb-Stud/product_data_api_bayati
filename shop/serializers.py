from rest_framework import serializers
from django.contrib.auth.models import User
from shop.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProductSerializer(serializers.ModelSerializer):
    """this is a simple product serializer for conversion between json and dictionaries into query sets
     and vice versa
    """
    class Meta:
        model = Product
        fields = ['id', 'title', 'picture', 'brand', 'category']


class VendorProductSerializer(serializers.ModelSerializer):
    """this is a simple VendorProduct serializer for conversion between json and dictionaries into query sets
     and vice versa
    """
    class Meta:
        model = Product
        fields = ['id', 'base_price', 'price', 'discount_percent', 'discount_price_difference', 'number_of_views', 'vendor', 'product']


class VendorSerializer(serializers.ModelSerializer):
    """just a serializer"""
    class Meta:
        model = Vendor
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    """just a serializer"""
    class Meta:
        model = Vendor
        fields = ['name', '']