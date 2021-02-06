# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.urls import reverse_lazy


from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, CreateView, UpdateView , DeleteView)
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
        context = super(EmployedDetailView, self).get_context_data(**kwargs)
        context['title'] = 'employee of month'
        print(context)
        return context


class SuccessView(TemplateView):
    template_name = "employed/succes_employe.html"


class EmployeCreateView(CreateView):
    model = Employed
    template_name = "employed/create_empoyed.html"
    # Mostrar los datos que quiero pintar en mi form
    fields = ['first_name', 'last_name', 'job', 'department', 'image', 'skill']
    # Muesta todos los atributos
    #fields = ('__all__')
    # cada ves que termine el proceso debe redirecionar a un url
    success_url = reverse_lazy('employed_app:creteSucces')
    # form valid recupero el object save

    def form_valid(self, form):
        # para que no haga dos save
        employed = form.save(commit=False)
        # employed = form.save()
        employed.full_name = employed.first_name + ' ' + employed.last_name
        # actualiza el object save
        employed.save()
        return super(EmployeCreateView, self).form_valid(form)


class EmployedUpdateView(UpdateView):
    model = Employed
    template_name = "employed/update_employed.html"
    fields = ['first_name', 'last_name', 'job', 'department', 'image', 'skill']
    success_url = reverse_lazy('employed_app:creteSucces')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # para que no haga dos save
        employed = form.save(commit=False)
        # employed = form.save()
        employed.full_name = employed.first_name + ' ' + employed.last_name
        # actualiza el object save
        employed.save()
        return super(EmployedUpdateView, self).form_valid(form)



class EmployedDeleteView(DeleteView):
    model = Employed
    template_name = "employed/deleteEmployed.html"
    success_url = reverse_lazy('employed_app:creteSucces')
