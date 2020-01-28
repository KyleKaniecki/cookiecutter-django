from django.contrib.admin.apps import AdminConfig

class {{cookiecutter.project_name}}AdminConfig(AdminConfig):
    default_site = '{{cookiecutter.project_slug}}.admin.{{cookiecutter.project_name}}AdminSite'