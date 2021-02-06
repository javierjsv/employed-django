# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView)
# Create your views here.


# http://ccbv.co.uk/  recursos para las listview
from .models import Employed


# lista empleados por trabajo

# listar habilidades de un empleado


# listar todos los empleados de la empresa
class AllListEmployed(ListView):
    template_name = 'employed/list_all.html'
    # paginacion
    paginate_by = 2
    model = Employed
    ordering = 'first_name'

    def get_paginate_by(self, queryset):
        number_page = self.request.GET.get('page', '')
        print('number', number_page)
        return self.paginate_by


# listar todos los empleados que pertencen a un area de la empresa
class ListEmployedbyArea(ListView):
    template_name = 'employed/list_employed_by_area.html'
   #  queryset = Employed.objects.filter(department__name='System' ) forma basica de hacer un filtro
   # obtener parametro por ulr

    def get_queryset(self):
        area = self.kwargs['name']
        # conjunto de register
        list = Employed.objects.filter(
            department__name=area
        )
        return list


# listar los empleados por palabra clave
class listEmployedByKeywod(ListView):
    template_name = 'employed/employedKeywor.html'
    context_object_name = 'employes'

    def get_queryset(self):
        print('**********')
        key_word = self.request.GET.get('name', '')
        print(key_word)
        list = Employed.objects.filter(
            first_name=key_word
        )
        print('list', list)
        return list


class listSkillEmployed(ListView):
    template_name = 'employed/listSkillEmployed.html'
    context_object_name = 'employes'
    # by id user

    def get_queryset(self):
        result_employed = Employed.objects.get(id=2)
        print(result_employed.skill.all())
        return result_employed.skill.all()


class EmployedDetailView(DetailView):
     model = Employed
     template_name = "employed/detail_employed.html"
     def get_context_data(self, **kwargs):
        context = super(EmployedDetailView , self).get_context_data(**kwargs)
        context['title'] = 'employee of month'  
        print(context)
        return context