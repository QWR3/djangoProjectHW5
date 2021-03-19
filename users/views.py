from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from company.serializers import CompanySerializer
UserModel = get_user_model()

# Create your views here.


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class CreateCompany(CreateAPIView):
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
