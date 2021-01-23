# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Department

# Register your models here.

# pasar tablas al admin , para que visualicen y personalizar

class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'short_name'
    )
    search_fields = ('name',)


admin.site.register(Department, DepartmentAdmin)
