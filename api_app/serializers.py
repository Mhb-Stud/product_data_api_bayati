from rest_framework import serializers
from .models import Product

# serializers are responsible for converting query sets and complex database types into json
# and simple python types your serializer should inherit from ModelSerializer from rest_framework
# package and you should specify the table that is going to be serialized by model field and
# the columns that you want from that table a serializer also can be used to deserialize data
# and convert python types into complex data types and write to database


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


