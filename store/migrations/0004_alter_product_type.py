# Generated by Django 5.0.1 on 2024-03-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_type_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.TextField(default='some text', max_length=1000),
        ),
    ]
