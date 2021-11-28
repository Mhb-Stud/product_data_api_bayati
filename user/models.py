from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    this model holds user data and overrides django default user also changed settings.py for config
    """
    username = models.CharField(primary_key=True, max_length=50)
    password = models.TextField()
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
