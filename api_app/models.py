from django.db import models


# for creating models your model class in this case person should inherit
# from Model class in django and after that dont forget to migrate
class Product(models.Model):
    product_id = models.IntegerField()
    product_title = models.TextField()
    product_price = models.TextField()
    price_before_discount = models.IntegerField()