# -*- coding: utf-8 -*-

from rest_framework import serializers
from ..models.m_products import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
