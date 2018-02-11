from django.shortcuts import render
from .models import ProductType, Product, Spec
from django.http import HttpResponse


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
    if not product:
        return HttpResponse('There is no product with id = {}'.format(pk), status=404)
    return render(request, 'product.html', context)
