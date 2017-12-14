# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import *

# Create your models here.
class Cliente(models.Model):
	BOOL_CHOICES = ((True, 'Sí'), (False, 'No'))

	DOC_TYPE_CHOICES = (('pasaporte','Pasaporte'),('cedula_identidad', 'Cédula de Identidad'),('cedula_residente','Cédula de Residente'))
	
	cedula = models.CharField(max_length=50, verbose_name="Número de Documento")
	tipo = models.CharField(max_length = 50, verbose_name = "Tipo de Documento", choices = DOC_TYPE_CHOICES, default="cedula_identidad")
	salario = models.FloatField(validators = [MinValueValidator(0.0)])
	tel1 = models.CharField(verbose_name = "Número de Teléfono 1", max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
	tel2 = models.CharField(verbose_name="Número de Teléfono 2", max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
	tel3 = models.CharField(verbose_name = "Número de Teléfono 3", max_length=8, validators=[RegexValidator(r'^\d{1,8}$')])
	buro = models.BooleanField(choices=BOOL_CHOICES)
	telefonica = models.BooleanField(choices=BOOL_CHOICES)

	def __unicode__(self):
		return "Cliente-"+self.cedula
	

