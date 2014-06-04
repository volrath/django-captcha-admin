from django.contrib import admin

from .forms import AdminAuthenticationForm


class AdminSite(admin.sites.AdminSite):
    login_form = AdminAuthenticationForm

admin.site = AdminSite()
