"""django2_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views.v_products import ProductsList, ProductsDetail
from .views.v_hello import Hello
from .views.v_hello_v2 import Hello_V2


urlpatterns = []

products = [
    path('products', ProductsList.as_view(), name='products-list'),
    path('products/<int:pk>', ProductsDetail.as_view(), name='products-detail')
]

hello = [
    path('hello', Hello.as_view(), name='hello'),
]

urlpatterns = products + hello


hello_v2 = [
    path('v2/hello', Hello_V2.as_view(), name='hello_v2'),
]

urlpatterns += hello_v2


