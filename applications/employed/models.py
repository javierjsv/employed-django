# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from applications.department.models import Department

# Create your models here.


class Employed(models.Model):
    # model for table  employed
    JOB_CHOICES = (
        ('1', 'CONTADOR'),
        ('2', 'ADMINISTRADOR'),
        ('3', 'ECONOMISTA'),
        ('4', 'OTRO'),
    )
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajos', max_length=1, choices=JOB_CHOICES)
    # 1 a muchos
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return str(self.id) + '  ' + self.first_name + ' ' + self.last_name
