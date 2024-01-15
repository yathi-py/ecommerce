from rest_framework import generics, permissions
from .models import Products
from .permissions import IsOwnerOrReadOnly, IsProductForLoggedInUser
from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    """
    API view for listing products using Django REST Framework's ListAPIView.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    """
    API view for creating products using Django REST Framework's CreateAPIView.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsProductForLoggedInUser]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting products using Django REST Framework's RetrieveUpdateDestroyAPIView.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
