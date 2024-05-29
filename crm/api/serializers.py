from rest_framework import serializers
from .models import Greetings
from django.contrib.auth.models import User


class GreetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greetings
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
