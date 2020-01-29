from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    {{cookiecutter.user_model_name}}Detail,
    {{cookiecutter.user_model_name}}List,
    PasswordReset,
    PasswordResetConfirm,
    ObtainTokenPairView,
)

urlpatterns = [
    path("{{cookiecutter.user_model_name}}s/", {{cookiecutter.user_model_name}}List.as_view()),
    path("{{cookiecutter.user_model_name}}s/<int:pk>/", {{cookiecutter.user_model_name}}Detail.as_view()),
    path("auth/token/", ObtainTokenPairView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
    path("password/reset/", PasswordReset.as_view()),
    path("password/reset/confirm/", PasswordResetConfirm.as_view()),
]
