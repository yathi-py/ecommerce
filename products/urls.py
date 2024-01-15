from django.urls import path
from .views import ProductListView, ProductCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(),
         name='product-retrieve-update-destroy'),
]
