from rest_framework.serializers import ModelSerializer
from .models import CustomCompany
from employee.serializers import EmployeeSerializer


class CompanySerializer(ModelSerializer):
    employee = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = CustomCompany
        exclude = ['user']
