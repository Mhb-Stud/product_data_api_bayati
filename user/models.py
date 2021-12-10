from django.db import models
from django.contrib.auth.models import (
    AbstractUser, BaseUserManager
)
from django.dispatch import receiver
from django.db.models.signals import (
    post_save
)


class UserQuerySet(models.QuerySet):
    pass

class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def create_user(self, username, email, first_name=None, last_name=None, password=None, password2=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        if password != password2:
            raise ValueError('Passwords did not Match!')
        else:
            user.set_password(password)
            user.save(using=self._db)
            return user


class User(AbstractUser):
    """this model holds user data and overrides django default user also changed settings.py for config
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.TextField()
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    objects = UserManager()



