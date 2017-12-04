# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cliente

# Register your models here.
admin.site.register(Cliente)

#Style
admin.site.site_header = "Administración - Créditos Telefónica"
admin.site.site_title = "Créditos Telefónica"
# admin.site.index_title


