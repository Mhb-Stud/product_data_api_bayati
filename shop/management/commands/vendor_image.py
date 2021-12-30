from django.core.management.base import BaseCommand
from django.core.files import File
import os
from io import BytesIO
from config.settings import BASE_DIR
from shop.models import Vendor
from PIL import Image
from django.db.models.fields.files import ImageFieldFile, FileField

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        self.get_category_image_files()

    def get_category_image_files(self):
        folder_path = os.path.join(BASE_DIR, 'media/vendor_logos')
        image_paths = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]
        for path in image_paths:
            with open(path, 'rb') as file:
                image = file.read()
            memory_file = BytesIO(image)
            extension = os.path.splitext(path)[-1]
            file_name = os.path.splitext(path)[0].rsplit('\\')[-1] + extension
            vendor_name = os.path.splitext(path)[0].rsplit('\\')[-1]
            to_be_saved = File(memory_file, name=file_name)
            self.save_to_database(vendor_name=vendor_name, to_be_saved=to_be_saved)

    def save_to_database(self, vendor_name, to_be_saved):
        try:
            vendor = Vendor.objects.get(name=vendor_name)
            if vendor.logo is None:
                vendor.logo = to_be_saved
                vendor.save()
        except Vendor.DoesNotExist:
            Vendor.objects.create(name=vendor_name, logo=to_be_saved)
