from rest_framework.serializers import ModelSerializer
from .models import CustomEmployee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = CustomEmployee
        exclude = ['company']
