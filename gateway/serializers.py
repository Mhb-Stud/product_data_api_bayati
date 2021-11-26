from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


"""
 serializers are responsible for converting query sets and complex database types into json
 and simple python types your serializer should inherit from ModelSerializer from rest_framework
 package and you should specify the table that is going to be serialized by model field and
 the columns that you want from that table a serializer also can be used to deserialize data
 and convert python types into complex data types and write to database
 """
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'base_price', 'vendor']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'vendor']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        corresponding_vendor = Vendor.objects.filter(name=validated_data['username'])
        if corresponding_vendor.count() == 1:
            corresponding_vendor[0].user = user
            corresponding_vendor[0].save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
