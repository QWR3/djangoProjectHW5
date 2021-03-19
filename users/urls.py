from django.urls import path, include
from .views import UserListCreateView, CreateCompany , UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='list create user'),
    path('/<int:pk>/company', UserListCreateView.as_view(), name='create company'),
    path('/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='update destroy user'),
]
