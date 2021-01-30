# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20)
    active = models.BooleanField('Activo', default=False,)

    class Meta:
        #verbose_name = 'My department'
        #verbose_name_plural = 'Area of the company'
        ordering = ['id']
        #Que no se puedean duplicar
        unique_together = ('name', 'short_name')

    def __str__(self):
        return  str(self.id) + ' ' + self.name + '  ' + self.short_name
