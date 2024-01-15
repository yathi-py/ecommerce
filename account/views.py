from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.GenericAPIView):
    """
    API view for user registration using the RegisterSerializer.
    """
    serializer_class = RegisterSerializer

    def post(self, request):
        """
        Handles POST requests for user registration.
        """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginApiView(generics.GenericAPIView):
    """
    API view for user login using the LoginSerializer.
    """
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Handles POST requests for user login.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
