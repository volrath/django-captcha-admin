from django.contrib import admin
from django.contrib.admin import autodiscover

from .sites import AdminSite

site = AdminSite()
admin.site = site
