# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from applications.department.models import Department

from ckeditor.fields import RichTextField

# Create your models here.


class Skill(models.Model):
    name = models.CharField('name', max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id) + ' ' + self.name


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
    # one to many
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatar', blank=True , null = True)
    #python -m pip install Pillow
    #many to many
    skill = models.ManyToManyField(Skill)
    #usando app de terceros
    curriculum = RichTextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '  ' + self.first_name + ' ' + self.last_name
