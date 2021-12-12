from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import VendorProduct
from .serializers import VendorProductSerializer
from rest_framework.response import Response


class ShopManager(viewsets.ViewSet):
    query_set = VendorProduct.objects.values('product__id',
                                             'base_price', 'price', 'discount_percent',
                                             'discount_price_difference', 'number_of_views', 'product__title',
                                             'product__brand__name', 'product__category__name')

    def list(self, request):
        serialized = self.query_set
        return Response(serialized)

    @action(methods=['GET'], detail=True, url_path='', url_name='get_productzzz')
    def get_product(self, request, pk=None):
        product = self.query_set.filter(product__id=pk)[0]
        product_queryset = VendorProduct.objects.filter(product_id=pk)
        product_queryset.update(number_of_views=product_queryset[0].number_of_views + 1)
        return Response(product)
