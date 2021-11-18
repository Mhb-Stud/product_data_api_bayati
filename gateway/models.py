from django.db import models


""" 
 for creating models your model class in this case person should inherit
 from Model class in django and after that dont forget to migrate
"""
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    price = models.IntegerField()
    base_price = models.IntegerField()
