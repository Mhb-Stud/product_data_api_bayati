from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        db_table = 'vendor'


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.TextField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    """ 
     for creating models your model class in this case person should inherit
     from Model class in django and after that dont forget to migrate
    """
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    base_price = models.IntegerField(default=0)
    vendor = models.ForeignKey(Vendor, max_length=50, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title



