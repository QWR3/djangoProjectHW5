from django.urls import path, include
from .views import CompanyListView, EmployeeCreateView, CompanyRetrieveUpdateDestroyView

urlpatterns = [
    path('', CompanyListView.as_view(), name='list_company'),
    path('/<int:pk>/employee', EmployeeCreateView.as_view(), name='Employee_create'),
    path('/<int:pk>', CompanyRetrieveUpdateDestroyView.as_view(), name='Retrieve Update Destroy company')
]

