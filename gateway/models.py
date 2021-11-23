from django.db import models


""" 
 for creating models your model class in this case person should inherit
 from Model class in django and after that dont forget to migrate
"""
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    base_price = models.IntegerField(default=0)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title

class Vendor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'vendor'


class ProductInstance:
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_instance'

