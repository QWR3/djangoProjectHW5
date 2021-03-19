from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from company.serializers import CompanySerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    company = CompanySerializer(many=True, required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'password', 'email', 'is_staff', 'is_superuser', 'is_active', 'company']

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
