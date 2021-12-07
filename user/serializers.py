from rest_framework import serializers
from django.contrib.auth.models import User
from shop.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    """just a serializer"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'vendor']


# class RegisterSerializer(serializers.ModelSerializer):
#     """this class is responsible for registering users and saving their model in the database
#     it also checks weather a vendor with the same name exists if it exists it maps the user
#     to the vendor with a oneToOne field
#     """
#     email = serializers.EmailField(
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
#
#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#
#         return attrs
