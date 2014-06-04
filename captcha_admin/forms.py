from django.contrib.admin.forms import (
    AdminAuthenticationForm as _AdminAuthenticationForm
)

from captcha.fields import ReCaptchaField


class AdminAuthenticationForm(_AdminAuthenticationForm):
    captcha = ReCaptchaField(attrs={'theme': 'clean'})
