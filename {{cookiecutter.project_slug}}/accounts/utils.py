from django.conf import settings
import pyotp

def get_otp_uri(user):
    return pyotp.totp.TOTP(settings.TWO_FACTOR_KEY).provisioning_uri(
        user.email, issuer_name="{{cookiecutter.project_name}}"
    )
