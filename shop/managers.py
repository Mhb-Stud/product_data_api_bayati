from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from rest_framework.response import Response
import shop.models as my_models
from shop.models import *


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

    def make_or_get(self, category_name):
        return self.get_or_create(name=category_name)


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
        return self.get_queryset().make_or_get(category_name)


class ProductQuerySet(models.QuerySet):
    def create_product(self, product):
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
        category = self.create_or_get_category(data['category_name'])
        brand = self.create_or_get_brand(data['brand'], category)
        product_info = {
            'id': data['id'],
            'title': data['name'],
            'brand': brand,
            'category': category,
        }
        product = ProcessManager.create_or_get_product(product_info)
        vendor = self.create_or_get_vendor(data['vendor'])
        ProcessManager.create_or_get_vendor_product(product, vendor, data)

    @staticmethod
    def create_or_get_brand(brand_name, brand_category):
        brand, created = my_models.Brand.objects.get_or_create(name=brand_name, category=brand_category)
        return brand

    @staticmethod
    def create_or_get_category(category_name):
        category, created = my_models.Category.objects.make_or_get(category_name=category_name)
        return category

    @staticmethod
    def create_or_get_vendor(name):
        vendor, created = my_models.Vendor.objects.get_or_create(name=name)
        return vendor

    @staticmethod
    def create_or_get_vendor_product(product, vendor, other_info):
        default = {
            'base_price': other_info['base_price'],
            'price': other_info['price'],
        }
        my_models.VendorProduct.objects.get_or_create(product=product, vendor=vendor, defaults=default)

    @staticmethod
    def create_or_get_product(data):
        product, created = my_models.Product.objects.get_or_create(id=data['id'], title=data['title'], brand=data['brand'], category=data['category'])
        return product
