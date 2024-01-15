from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration, extending the base ModelSerializer provided by Django REST Framework.
    """
    password = serializers.CharField(max_length=68, min_length=6,
                                     write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        """
        Custom validation method to ensure the username is alphanumeric.
        """
        email = attrs.get("email", '')
        username = attrs.get("username", '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should be alphanumeric')
        return attrs

    def create(self, validated_data):
        """
        Creates and returns a new user instance using the provided validated data.
        """
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer for user login, extending the base ModelSerializer provided by Django REST Framework.
    """
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, min_length=6,
                                     write_only=True)
    username = serializers.CharField(max_length=255, min_length=3,
                                     read_only=True)
    tokens = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        """
        Custom validation method to authenticate the user based on provided email and password.
        """
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials')

        if not user.is_active:
            raise AuthenticationFailed('User not active')

        if not user.is_verified:
            raise AuthenticationFailed('User not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }
