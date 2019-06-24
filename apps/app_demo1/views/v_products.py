# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from ..models.m_products import Products
from ..serializers.s_products import ProductsSerializer
from rest_framework import generics
from django_filters import rest_framework as filters


class ProductsFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='gte')

    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'count', 'ctime', 'mtime', 'min_price', 'max_price']


class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductsFilter


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer