from .passwordreset import PasswordReset
from .passwordresetconfirm import PasswordResetConfirm
from .{{cookiecutter.user_model_name_lower}}detail import {{cookiecutter.user_model_name}}Detail
from .{{cookiecutter.user_model_name_lower}}list import {{cookiecutter.user_model_name}}List
from .obtaintokenpair import ObtainTokenPairView

__all__ = [
    "{{cookiecutter.user_model_name}}Detail",
    "{{cookiecutter.user_model_name}}List",
    "PasswordReset",
    "PasswordResetConfirm",
    "ObtainTokenPairView",
]
