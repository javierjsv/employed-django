# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.views.generic import (TemplateView , ListView  , CreateView)
# Create your views here.

# Models

from .models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = 'home/list.html'
    context_object_name = 'listNumber'
    queryset = ['0' , '2' , '3']


class PruebaListModel(ListView):
    template_name = "home/pruebaList.html"
    model = Prueba
    context_object_name  = 'listPrueba'



class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields = ['title', 'subtitle','quantity']
