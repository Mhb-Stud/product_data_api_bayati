from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class CategoryQuerySet(models.QuerySet):
    def get_super_category(self, name):
        super_category = None
        try:
            super_category = self.get(name=name)
        except ObjectDoesNotExist as ex:
            print('crawler is buggy!')

        return super_category

    def create_category(self, data):
        return self.create()

class CategoryManager(models.Manager):

    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def create_category(self, data):
        super_category_name = data['super_category']
        category = None
        if super_category_name is not None:
            super_category = self.get_queryset().get_super_category(super_category_name)
        return self.get_queryset().create_category(data)

    def product_or_category(self, data):
        return None

    def main(self, data):
        if data['vendor'] is None:
            self.create_category(data)
