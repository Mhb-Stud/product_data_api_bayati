from django.db import models
from user.models import User


class Vendor(models.Model):
    """
    stores vendor information and connects vendor to user by a one to one field this means that each user is a vendor
    and each vendor is a user although this model is created for now and later on if we wanted to have normal users
    we can extend the user model and create two types of users
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, to_field='username', null=True)
    logo = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = 'vendor'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)


class Product(models.Model):
    """
    this model stores product information in the database also we have a vendor field as foreignKey that shows each product
    has a vendor to be sure for each product i add i check weather it's vendor exists in the database or not if not i create
    it's vendor in the database
    """
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'product'
        indexes = [
            models.Index(fields=['title'], name='title idx')
        ]

    def __str__(self):
        return self.title


class ProductAttribute:
    id = models.AutoField(primary_key=True)
    title = models.CharField()
    value = models.CharField()
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)

    class Meta:
        verbose_name_plural = ("Attributes",)


class VendorProduct(models.Model):
    id = models.AutoField(primary_key=True)
    base_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    discount_percent = models.FloatField(default=0)
    discount_price_difference = models.FloatField(default=0)
    number_of_views = models.IntegerField(default=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)


