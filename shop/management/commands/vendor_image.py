from django.core.management.base import BaseCommand
from django.core.files import File
import os
from config.settings import BASE_DIR
from shop.models import Category
from PIL import Image
from django.db.models.fields.files import ImageFieldFile, FileField
import wget
from shop.models import Vendor

class Command(BaseCommand):
    help = 'gets and copies vendor images to db'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(BASE_DIR, 'shop/management/commands/vendor_image_link.txt')
        with open(file_path, 'r') as file:
            while file:
                url = file.readline().replace('\n', '')
                vendor_name = file.readline().replace('\n', '')
                file_name = vendor_name + os.path.splitext(url)[-1]
                self.download_vendor_photo_and_save(url, vendor_name, file_name)

    def download_vendor_photo_and_save(self, photo_url, vendor_name, file_name):
        store_path = f'media/vendor_logos/{file_name}'
        response = wget.download(photo_url, out=store_path)
        try:
            my_object = Vendor.objects.get(name=vendor_name)
            my_object.logo = response
            my_object.save()
        except Vendor.DoesNotExist:
            Vendor.objects.create(name=vendor_name, logo=response)