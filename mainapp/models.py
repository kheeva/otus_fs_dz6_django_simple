from django.db import models

# Create your models here.
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
    type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    img_url = models.CharField(verbose_name='Фото', max_length=150)

    def __str__(self):
        return self.name


class Spec(models.Model):
    type_id = models.ForeignKey(SpecType, on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение свойства', max_length=50)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.type_id, self.value)


"""
class MainModel(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=32, null=True)
    title = models.CharField(verbose_name='Title', max_length=32, null=True)
    birth_day = models.DateField(verbose_name='Дата рождения', null=True)
    birth_day_old = models.CharField(verbose_name='Дата рождения по старому календарю', max_length=32, null=True)
    death_day = models.DateField(verbose_name='Дата смерти', null=True)
    death_day_old = models.CharField(verbose_name='Дата смерти по старому календарю',max_length=32, null=True)
    description = models.TextField(verbose_name='Описание', null=True)
    page = models.CharField(verbose_name='Код страницы', max_length=16, null=True)

    def __str__(self):
        return self.name


class StudiesModel(models.Model):
    name = models.CharField(verbose_name='Заголовок', max_length=32, null=True)
    title = models.CharField(verbose_name='Title', max_length=32, null=True)
    page = models.CharField(verbose_name='Код страницы', max_length=16, null=True)

    def __str__(self):
        return self.name


class StudiesTextsModel(models.Model):
    study = models.ForeignKey(StudiesModel, verbose_name='Учеба', related_name='texts')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.study.name
"""


"""class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    img_url = db.Column(db.String(100))

    specs = db.relationship('Spec',
                            backref=db.backref('product', lazy=True))

    def __repr__(self):
        return '<Product %r>' % self.name

class ProductType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Spec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('spec_type.id'))
    value = db.Column(db.String(50))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    spec_type = db.relationship('SpecType',
                                backref=db.backref('spec', lazy=True))

    def __repr__(self):
        return '<Spec %r %r>' % (self.type_id, self.value)

class SpecType(db.Model):
    id = db.Column(db.Integer, primary_key=True)

name = db.Column(db.String(50), unique=True, nullable=False)"""
