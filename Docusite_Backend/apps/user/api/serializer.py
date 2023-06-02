from rest_framework import serializers
from ..models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('rol', 'username', 'email', 'first_name', 'last_name')


class UserListRetrieveDestroySerializer(serializers.ModelSerializer):

    rol = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('uuid', 'rol', 'username', 'email', 'first_name', 'last_name', 'is_active')

    def get_rol(self, obj):
        return {
            'code': obj.rol,
            'description': obj.get_rol_display()
        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """SIMPLE JWT SERIALIZER TO RETORN THE USER DATA AND TOKEN"""
    def validate(self, attrs):
        data = super().validate(attrs)
        user_serializer = UserListRetrieveDestroySerializer(self.user) 
        data["user"] = user_serializer.data
        return data
