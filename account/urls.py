from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, \
    TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import RegisterView, LoginApiView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]