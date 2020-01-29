from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


from .models import {{cookiecutter.user_model_name}}

# Register your models here.


class {{cookiecutter.user_model_name}}AdminConsole(UserAdmin):
    list_display = ("id", "username", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


# We need to add these here since they are registered with the default Django admin
admin.site.register({{cookiecutter.user_model_name}}, {{cookiecutter.user_model_name}}AdminConsole)
