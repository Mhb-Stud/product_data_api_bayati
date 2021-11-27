from django.db import models
from django.contrib.auth.models import AbstractUser

"""
this model holds user data and overrides django default user also changed settings.py for config
"""
class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=300)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)


"""
stores vendor information and connects vendor to user by a one to one field this means that each user is a vendor
and each vendor is a user although this model is created for now and later on if we wanted to have normal users
we can extend the user model and create two types of users
"""
class Vendor(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, to_field='username', null=True)

    class Meta:
        db_table = 'vendor'


""" 
this model stores product information in the database also we have a vendor field as foreignKey that shows each product
has a vendor to be sure for each product i add i check weather it's vendor exists in the database or not if not i create
it's vendor in the database 
"""
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    base_price = models.IntegerField(default=0)
    vendor = models.ForeignKey(Vendor, max_length=50, on_delete=models.CASCADE, to_field='name')

    class Meta:
        db_table = 'product'
        indexes = [
            models.Index(fields=['title'], name='title idx')
        ]

    def __str__(self):
        return self.title



