from django.db import models
from company.models import CustomCompany


# Create your models here.
class CustomEmployee(models.Model):
    class Meta:
        db_table = 'employee'

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    profession = models.CharField(max_length=25)
    age = models.IntegerField()
    company = models.ForeignKey(CustomCompany, on_delete=models.CASCADE, related_name='employee')
