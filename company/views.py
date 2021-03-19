from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from .serializers import CompanySerializer
from .models import CustomCompany
from employee.serializers import EmployeeSerializer
from employee.models import CustomEmployee


# CustomCompany
# Create your views here.

class CompanyListView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = CustomCompany.objects.all()


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        company_id = self.kwargs.get('pk')
        company = get_object_or_404(CustomCompany, pk=company_id)
        serializer.save(company=company)


class CompanyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = CustomCompany.objects.all()
