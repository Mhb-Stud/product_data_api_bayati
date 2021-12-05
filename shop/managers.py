from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from .serializers import *
from rest_framework.response import Response


class CategoryQuerySet(models.QuerySet):
    def get_super_category(self, name):
        super_category = None
        try:
            super_category = self.get(name=name)
        except ObjectDoesNotExist as ex:
            print('crawler is buggy!')

        return super_category

    def create_category(self, name, super_category=None):
        return self.create(name=name, super_category=super_category)


class CategoryManager(models.Manager):

    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def create_for_crawler(self, data):
        super_category_name = data['super_category']
        category_name = data['name']
        if super_category_name is not None:
            super_category = self.get_queryset().get_super_category(super_category_name)
            return self.get_queryset().create_category(category_name, super_category)
        return self.get_queryset().create_category(category_name)

    def process_category(self, data):
        self.create_for_crawler(data)

    def make_or_get(self, category_name):
        return self.get_queryset().get_or_create(name=category_name)


class ProductQuerySet(models.QuerySet):
    def create_product(self, product):
        serialized = ProductSerializer(product)
        if serialized.is_valid():
            return self.create(id=product['id'], title=product['title'], brand=product['brand'], category=product['category'])


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def process_product(self, data):
        self.create_product(data)

    def create_product(self, data):
        return self.get_queryset().create_product(data)

class ProcessManager(models.Manager):
    def process(self, data):
        brand = self.create_brand(data['brand'])
        category = self.create_or_get_category(data['category_name'])
        product = {
            'id': data['id'],
            'title': data['title'],
            'brand': brand,
            'category': category,
        }
        Product.objects.create_product(product)

    @staticmethod
    def create_brand(brand_name):
        return Brand.objects.create(name=brand_name)

    def create_or_get_category(self, category_name):
        return CategoryManager.make_or_get(category_name)
