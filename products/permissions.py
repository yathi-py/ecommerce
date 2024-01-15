from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

from account.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.

    This permission class checks whether the user making the request is the owner of the object.
    Owners are allowed to perform any request, while other users can only perform safe methods (GET, HEAD, OPTIONS).

    Attributes:
        - request: The HTTP request object.
        - view: The Django REST Framework view.
        - obj: The object being accessed or modified.

    Methods:
        - has_object_permission(self, request, view, obj): Determines if the user has permission to access or modify the object.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user is the owner of the object.

        Args:
            - request: The HTTP request object.
            - view: The Django REST Framework view.
            - obj: The object being accessed or modified.

        Returns:
            - bool: True if the user has permission, False otherwise.

        Raises:
            - PermissionDenied: If the user does not have permission.
        """
        owner = get_object_or_404(User, id=obj.user)

        if request.method in permissions.SAFE_METHODS:
            return True

        user_id = request.data.get('user')
        if user_id and user_id != owner.id:
            message = ("You do not have permission to create/edit a "
                       "product for another user, Please check your user id")
            raise PermissionDenied(detail=message)

        return owner == request.user


class IsProductForLoggedInUser(permissions.BasePermission):
    """
    Custom permission to only allow access to the logged-in user.

    This permission class checks whether the user making the request is the same as the owner of the product.

    Attributes:
        - request: The HTTP request object.
        - view: The Django REST Framework view.

    Methods:
        - has_permission(self, request, view): Determines if the user has permission to access the view.
    """

    def has_permission(self, request, view):
        """
        Check if the requesting user is the owner of the product.

        Args:
            - request: The HTTP request object.
            - view: The Django REST Framework view.

        Returns:
            - bool: True if the user has permission, False otherwise.

        Raises:
            - PermissionDenied: If the user does not have permission.
        """
        try:
            owner = User.objects.get(id=request.data.get('user'))
        except User.DoesNotExist:
            message = "User in product Not Found"
            raise PermissionDenied(detail=message)

        if request.user != owner:
            message = ("You do not have permission to create"
                       " a product for another user.")
            raise PermissionDenied(detail=message)

        return True
