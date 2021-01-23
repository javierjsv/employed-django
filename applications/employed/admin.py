# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Employed, Skill


class EmployedAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'job',
        'department'
    )


admin.site.register(Employed, EmployedAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

admin.site.register(Skill, SkillAdmin)
