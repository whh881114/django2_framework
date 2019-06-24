# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.m_products import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'ctime', 'mtime')

admin.site.register(Products, ProductsAdmin)