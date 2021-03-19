from django.urls import path, include
from .views import EmployeeListView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('', EmployeeListView, name='list employee'),
    path('/<int:pk>', EmployeeRetrieveUpdateDestroyView, name='Retrieve Update Destroy View employee'),
]
