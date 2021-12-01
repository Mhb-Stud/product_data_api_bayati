from django.core.exceptions import ObjectDoesNotExist
from django.db import models
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

    def create_category(self, data):
        super_category_name = data['super_category']
        category_name = data['name']
        if super_category_name is not None:
            super_category = self.get_queryset().get_super_category(super_category_name)
            return self.get_queryset().create_category(category_name, super_category)
        return self.get_queryset().create_category(category_name)

    # def product_or_category(self, data):
    #     return None

    def main(self, data):
        if 'vendor' is not data:
            self.create_category(data)
