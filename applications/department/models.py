# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20)
    active = models.BooleanField('Activo', default=False , unique=True)
    
    def __str__(self):
        return self.name + '-' + self.short_name
