# Generated by Django 5.0.1 on 2024-03-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='id',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='user',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
