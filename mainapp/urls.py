from django.conf.urls import url
from django.urls import path

from mainapp.views import ProductsListView, ProductView

urlpatterns = [
    url(r'^$', ProductsListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    ]
