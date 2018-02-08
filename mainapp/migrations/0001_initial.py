# Generated by Django 2.0.2 on 2018-02-08 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('img_url', models.CharField(max_length=150, verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Значение свойства')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SpecType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Свойство')),
            ],
        ),
        migrations.AddField(
            model_name='spec',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.SpecType'),
        ),
        migrations.AddField(
            model_name='product',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductType'),
        ),
    ]