from django.conf.urls import url
from django.urls import path

from mainapp.views import products_list, product

urlpatterns = [
    url(r'^$', products_list, name='products_list'),
    # url(r'^product/(\d+)/$', product, name='product'),
    path('product/<int:pk>/', product, name='product'),
    ]
