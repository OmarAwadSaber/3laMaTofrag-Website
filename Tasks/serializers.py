from rest_framework import serializers
from .models import Task, customUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        return token

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = customUser
        fields = ('id', 'username', 'email', 'profilePhoto', 'isAdmin', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'isAdmin': {'read_only': True}  # Don't let users self-assign admin status
        }


    def create(self, validated_data):
        # Hash the password properly
        validated_data['password'] = make_password(validated_data['password'])
        return customUser.objects.create(**validated_data)
