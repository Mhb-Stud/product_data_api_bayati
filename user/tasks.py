from __future__ import absolute_import, unicode_literals

from celery import shared_task
from shop.models import Vendor
import wget

@shared_task
def download_vendor_photo(photo_url, username):
    response = wget.download(photo_url, out='media/vendor/images')
    my_object = None
    try:
        my_object = Vendor.objects.get(name=username)
    except Vendor.DoesNotExist:
        print("user is not a vendor!")
    my_object.logo = response
    my_object.save()
