from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import VendorProduct
from .serializers import VendorProductSerializer
from rest_framework.response import Response
from .tasks import increment_product_view


class ShopManager(viewsets.ViewSet):
    """this class is responsible for returning a single product and also returning all of the shop products"""
    query_set = VendorProduct.objects.get_vendor_products_with_detail()

    def list(self, request):
        """returns all products"""
        serialized = self.query_set
        return Response(serialized)

    @action(methods=['GET'], detail=True, url_path='', url_name='get_product')
    def get_product(self, request, pk=None):
        """with action decorator it creates a route in the router for getting a single product also i'll increment
        product view by one here
        """
        product = self.query_set.filter(product__id=pk)[0]
        # product_queryset = VendorProduct.objects.filter(product_id=pk)
        # product_queryset.update(number_of_views=product_queryset[0].number_of_views + 1)
        increment_product_view.delay(pk)
        return Response(product)
