from django.db import models
from django.contrib.auth.models import (
    AbstractUser, BaseUserManager
)
from django.dispatch import receiver
from django.db.models.signals import (
    post_save
)
from shop.models import Vendor


class UserQuerySet(models.QuerySet):
    pass

class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def create_user(self, username, email, first_name='', last_name='', password=None, password2=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        if password != password2:
            raise ValueError('Passwords should Match!')
        else:
            user.set_password(password)
            user.save(using=self._db)
            return user


class User(AbstractUser):
    """this model holds user data and overrides django default user also changed settings.py for config
    """
    username = models.CharField(primary_key=True, max_length=50)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    objects = UserManager()


@receiver(post_save, sender=User)
def map_vendor_user(sender, instance, created, *args, **kwargs):
    corresponding_vendor = Vendor.objects.filter(name=instance.username)
    if corresponding_vendor.count() == 1:
        corresponding_vendor[0].user = instance
        corresponding_vendor[0].save()

