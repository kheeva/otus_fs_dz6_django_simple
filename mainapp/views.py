from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ProductType, Product, Spec


class ProductsListView(View):
    def get(self, request):
        product_types = ProductType.objects.all()
        products = Product.objects.all()
        context = {
            'product_types': product_types,
            'products': products,
            }
        return render(request, 'index.html', context)


class ProductView(View):
    def get(self, request, pk=None):
        product = Product.objects.filter(pk=pk).first()
        product_specs = Spec.objects.filter(product_id=product)
        context = {
            'product': product,
            'product_specs': product_specs,
            }
        if not product:
            return HttpResponse('There is no product with id = {}'.format(pk), status=404)
        return render(request, 'product.html', context)
