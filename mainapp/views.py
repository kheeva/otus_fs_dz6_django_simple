# coding: utf-8
from django.shortcuts import render
from .models import ProductType, Product, Spec

# Create your views here.
def products_list(request):
    product_types = ProductType.objects.all()
    products = Product.objects.all()
    context = {
        'product_types': product_types,
        'products': products,
        }
    return render(request, 'index.html', context)


def product(request, pk=None):
    product = Product.objects.filter(pk=pk).first()
    product_specs = Spec.objects.filter(product_id=product)
    context = {
        'product': product,
        'product_specs': product_specs,
        }
    return render(request, 'product.html', context)
