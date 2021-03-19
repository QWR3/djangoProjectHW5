from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import CustomEmployee
from .serializers import ModelSerializer


# Create your views here.


class EmployeeListView(ListAPIView):
    queryset = CustomEmployee
    serializer_class = ModelSerializer


class EmployeeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CustomEmployee
    serializer_class = ModelSerializer
