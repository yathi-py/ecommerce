from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

from account.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.

    This permission class checks whether the user making the request is the owner of the object.
    Owners are allowed to perform any request, while other users can only perform safe methods (GET, HEAD, OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user is the owner of the object.
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
    """

    def has_permission(self, request, view):
        """
        Check if the requesting user is the owner of the product.
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
