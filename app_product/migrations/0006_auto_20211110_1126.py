# Generated by Django 3.2.8 on 2021-11-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0005_auto_20211030_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valuesofspecification',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.ManyToManyField(blank=True, to='app_product.ValuesOfSpecification', verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='type_filter',
            field=models.CharField(choices=[('base', 'Основной'), ('custom', 'Кастомный')], default='base', max_length=64, verbose_name='Тип фильтра'),
        ),
    ]
