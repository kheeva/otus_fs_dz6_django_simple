from django.contrib import admin
from .models import ProductType, Product, SpecType, Spec


admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(SpecType)
admin.site.register(Spec)
