from django.db import models

# a model for person to be added as a table to the database by django
# for creating models your model class in this case person should inherit
# from Model class in django and after that dont forget to migrate


class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    is_male = models.BooleanField()
