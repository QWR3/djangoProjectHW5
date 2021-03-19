from django.contrib.auth.models import AbstractBaseUser, PermissionManager
from django.db import models
from .managers import CustomUserManager


# Create your models here.
class UserModel(AbstractBaseUser, PermissionManager):
    class Meta:
        db_table = 'user'

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
