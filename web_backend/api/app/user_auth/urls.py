from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import register_view, login_view

urlpatterns = [
    path("login/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login")
]
