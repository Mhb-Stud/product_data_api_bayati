from __future__ import absolute_import, unicode_literals

from celery import shared_task
from shop.models import VendorProduct


@shared_task
def increment_product_view(primary_key):
    VendorProduct.objects.increment_vendor_product_views(primary_key)
