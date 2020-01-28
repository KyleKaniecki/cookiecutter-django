from django.conf import settings


def settings_context(_request):
    if settings.PRODUCTION:
        env_name = "PRODUCTION"
        env_color = "red"
    elif settings.STAGING:
        env_name = "STAGING"
        env_color = "orange"
    else:
        env_name = "LOCAL"
        env_color = "darkgrey"

    return {
        "settings": settings,
        "ENVIRONMENT_NAME": env_name,
        "ENVIRONMENT_COLOR": env_color,
    }
