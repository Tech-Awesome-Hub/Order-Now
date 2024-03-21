# Generated by Django 5.0.1 on 2024-03-21 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_producttype_rename_sub_category_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type_description',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='some text', max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='store.producttype'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='description',
            field=models.CharField(default='some text..', max_length=50),
        ),
    ]
