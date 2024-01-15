from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Products model using Django REST Framework's ModelSerializer.
    """
    class Meta:
        model = Products
        fields = '__all__'
