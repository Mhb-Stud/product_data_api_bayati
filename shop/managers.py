from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import F
from rest_framework.response import Response
import shop.models as my_models
from shop.models import *
from user.models import *


class CategoryQuerySet(models.QuerySet):
    def get_super_category(self, name):
        super_category = None
        try:
            super_category = self.get(name=name)
        except Category.DoesNotExist:
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


class VendorProductQuerySet(models.QuerySet):
    pass


class VendorProductManager(models.Manager):
    def get_queryset(self):
        return VendorProductQuerySet(self.model, using=self._db)

    def get_vendor_products_by_view(self, username):
        return self.get_queryset().order_by('-number_of_views'
                                            ).values('product__id',
                                                     'base_price', 'price', 'discount_percent',
                                                     'discount_price_difference', 'number_of_views', 'product__title',
                                                     'product__brand__name', 'product__category__name').filter(vendor__name=username)

    def get_vendor_products_with_detail(self):
        return self.get_queryset().values('product__id',
                                          'base_price', 'price', 'discount_percent',
                                          'discount_price_difference', 'number_of_views', 'product__title',
                                          'product__brand__name', 'product__category__name')

    def increment_vendor_product_views(self, primary_key):
        vendor_product = self.get_queryset().filter(product_id=primary_key)
        vendor_product.update(number_of_views=F('number_of_views') + 1)
        # try:
        #     my_object = self.get_queryset().get(product_id=primary_key)
        #     my_object.number_of_views = my_object.number_of_views + 1
        #     my_object.save()
        # except my_models.VendorProduct.DoesNotExist:
        #     print("user is not a vendor!")


class CrawlerProductProcessor(models.Manager):

    @classmethod
    def process(cls, data):
        category = cls.create_or_get_category(data['category_name'])
        brand = cls.create_or_get_brand(data['brand'], category)
        product_info = {
            'id': data['id'],
            'title': data['name'],
            'brand': brand,
            'category': category,
        }
        product = cls.create_or_get_product(product_info)
        vendor = cls.create_or_get_vendor(data['vendor'])
        cls.create_or_get_vendor_product(product, vendor, data)

    @classmethod
    def create_or_get_brand(cls, brand_name, brand_category):
        brand = None
        try:
            brand, created = my_models.Brand.objects.get_or_create(name=brand_name, defaults={'category': brand_category})
        except my_models.Brand.DoesNotExist:
            print("created brand!")
        return brand

    @staticmethod
    def create_or_get_category(category_name):
        category, created = my_models.Category.objects.make_or_get(category_name=category_name)
        return category

    @classmethod
    def create_or_get_vendor(cls, name):
        vendor, created = my_models.Vendor.objects.get_or_create(name=name)
        cls.map_vendor_to_existing_user(vendor)
        return vendor

    @staticmethod
    def create_or_get_vendor_product(product, vendor, other_info):
        default = {
            'base_price': other_info['base_price'],
            'price': other_info['price'],
            'id': other_info['id'],
        }
        my_models.VendorProduct.objects.get_or_create(product=product, vendor=vendor, defaults=default)

    @staticmethod
    def create_or_get_product(data):
        product = None
        try:
            default = {
                'category': data['category'],
                'brand': data['brand'],
                'id': data['id'],
            }
            product, created = my_models.Product.objects.get_or_create(id=data['id'], title=data['title'], defaults=default)
        except my_models.Product.DoesNotExist:
            print('product created!')
        return product

    @classmethod
    def map_vendor_to_existing_user(cls, vendor):
        users = User.objects.filter(username=vendor.name)
        if users.count() == 1:
            vendor.user = users[0]
            vendor.save()
