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
        'department',
        'full_name',
    )
    # Adicionar columna que no existe en el model

    def full_name(self, employ):
        return employ.first_name + ' ' + employ.last_name

    search_fields = ('first_name', 'last_name')
    list_filter = ('job', 'department', 'skill')
    # buscador solo para many to many
    filter_horizontal = ('skill',)


admin.site.register(Employed, EmployedAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    search_fields = ('name',)


admin.site.register(Skill, SkillAdmin)
