from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Custom{{ cookiecutter.user_model_name }}Manager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class {{cookiecutter.user_model_name}}(AbstractUser):

    objects = Custom{{cookiecutter.user_model_name}}Manager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
