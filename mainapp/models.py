from django.db import models


class ProductType(models.Model):
    name = models.CharField(verbose_name='Тип', max_length=150, unique=True)

    def __str__(self):
        return self.name


class SpecType(models.Model):
    name = models.CharField(verbose_name='Свойство', max_length=150, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150, unique=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    img_url = models.ImageField(verbose_name='Фото', max_length=150)

    def __str__(self):
        return self.name


class Spec(models.Model):
    type = models.ForeignKey(SpecType, on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение свойства', max_length=50)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.type, self.value)
