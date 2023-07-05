from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CreateUserView, ReadUserView, UpdateUserView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", CreateUserView.as_view(), name="register"),
    path("api/me/", ReadUserView.as_view(), name="me"),
    path("api/update_user_info/", UpdateUserView.as_view(), name="update_user_info"),
]
