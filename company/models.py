from django.db import models
from django.contrib.auth import get_user_model

# from users.models import CustomUsers

# Create your models here.
UserModel = get_user_model()


class CustomCompany(models.Model):
    class Meta:
        db_table = 'company'

    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='company')

