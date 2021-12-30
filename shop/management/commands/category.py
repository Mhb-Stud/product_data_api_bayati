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
            image = Image.open(path)
            memory_file = BytesIO()
            extension = os.path.splitext(path)[-1].replace('.', '')
            file_name = os.path.splitext(path)[0].rsplit('\\')[-1]
            image.save(memory_file, extension)
            to_be_saved = File(memory_file, name=file_name)
            try:
                vendor = Vendor.objects.get(name=file_name)
                vendor.logo = to_be_saved
                vendor.save()
            except Vendor.DoesNotExist:
                Vendor.objects.create(name=file_name, logo=to_be_saved)

    # def add_to_database(self, images):
    #     for image in images:
    #         category_name = image.filename.rsplit('\\')[-1].replace('.webp', '')
    #         imagefield = ImageFieldFile(instance=None, field=FileField(),
    #                                     name='shop/static/category/images/' + category_name + '.webp')
    #         try:
    #             category = Category.objects.get(name=category_name)
    #             category.logo = imagefield
    #             category.save()
    #         except Category.DoesNotExist:
    #             Category.objects.create(name=category_name, logo=imagefield)
    #
    #     self.stdout.write("script finished with code 0")
