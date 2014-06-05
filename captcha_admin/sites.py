from django.contrib.admin.sites import AdminSite as _AdminSite

from .forms import AdminAuthenticationForm


class AdminSite(_AdminSite):
    login_form = AdminAuthenticationForm
    login_template = 'admin/captcha_login.html'
