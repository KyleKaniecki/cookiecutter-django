import pyotp
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.admin import AdminSite
from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils import timezone
from django.utils.translation import ugettext_lazy


class TwoFactorAuthForm(AdminAuthenticationForm):

    otp = forms.CharField(required=False)

    def clean_otp(self):
        User = get_user_model()
        try:
            user = User.objects.get(username=self.cleaned_data.get("username"))
        except User.DoesNotExist:
            return
        code = self.cleaned_data.get("otp")
        totp = pyotp.TOTP(settings.TWO_FACTOR_KEY)
        if not (code == totp.now() or settings.DEBUG):
            raise forms.ValidationError("OTP does not match")
        return self.cleaned_data


class {{cookiecutter.project_name}}AdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy("{{cookiecutter.project_name}} Administartion")

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy("{{cookiecutter.project_name}} administration")

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy("{{cookiecutter.project_name}} administration")

    login_form = TwoFactorAuthForm

    login_template = "otp_admin_template.html"
