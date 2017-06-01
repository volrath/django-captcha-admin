from django.contrib import admin
from django.contrib.admin import autodiscover
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from .sites import AdminSite

site = AdminSite()
admin.site = site
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
