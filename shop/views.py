from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response


class ShopManager(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serialized = ProductSerializer(self.queryset, many=True)
        return Response(serialized.data)

    @action(methods=['GET'], detail=True, url_path='', url_name='get_productzzz')
    def get_product(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serialized = ProductSerializer(product)
        return Response(serialized.data)
