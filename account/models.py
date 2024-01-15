from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    """
    Custom manager for the User model, providing methods to create regular users
    and superusers with appropriate permissions.
    """

    def create_user(self, username, email, password=None):
        """
        Creates and saves a regular user with the given username, email, and password.

        :param username: The username for the new user.
        :param email: The email address for the new user.
        :param password: The password for the new user.
        :return: The created user instance.
        """
        if username is None:
            raise TypeError('User should enter user name')
        if email is None:
            raise TypeError('User should enter email')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_verified = True
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given username, email, and password.

        :param username: The username for the new superuser.
        :param email: The email address for the new superuser.
        :param password: The password for the new superuser.
        :return: The created superuser instance.
        """
        if password is None:
            raise TypeError('Password cant be none')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model with email as the unique identifier instead of the default username.
    """
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
    """
    Custom manager for the User model.
    """

    def __str__(self):
        """
        Returns a string representation of the User instance.

        :return: The email of the user.
        """
        return self.email

    def tokens(self):
        """
        Generates and returns authentication tokens for the user.

        :return: A dictionary containing the refresh and access tokens.
        """
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
