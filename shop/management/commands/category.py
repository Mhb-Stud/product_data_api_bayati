from django.core.management.base import BaseCommand
from django.core.files import File
import os
from config.settings import BASE_DIR
from shop.models import Category
from PIL import Image
from django.db.models.fields.files import ImageFieldFile, FileField

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        images = self.get_category_image_files()
        self.add_to_database(images)

    def get_category_image_files(self):
        folder_path = os.path.join(BASE_DIR, 'shop\\static\\category\\images')
        image_paths = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]
        images = []
        for path in image_paths:
            # with open(path, 'r') as file:
            #     image = file
            image = Image.open(path)
            images.append(image)

        self.stdout.write("images successfully retrieved")
        return images

    def add_to_database(self, images):
        for image in images:
            category_name = image.filename.rsplit('\\')[-1].replace('.webp', '')
            imagefield = ImageFieldFile(instance=None, field=FileField(),
                                        name='shop/static/category/images/' + category_name + '.webp')
            try:
                category = Category.objects.get(name=category_name)
                category.logo = imagefield
                category.save()
            except Category.DoesNotExist:
                Category.objects.create(name=category_name, logo=imagefield)

        self.stdout.write("script finished with code 0")
