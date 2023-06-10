from rest_framework import serializers
from ..models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('rol', 'username', 'email', 'first_name', 'last_name', 'password')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['password']
        return representation
    
    def validate_rol(self, value):
        if value is "SU":
            raise serializers.ValidationError("User can not be SuperAdmin")
        return value

    def create(self, validated_data):
        modelclass = self.Meta.model.objects.create_user(**validated_data)
        return modelclass


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
