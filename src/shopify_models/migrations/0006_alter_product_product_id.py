# Generated by Django 3.2.6 on 2021-11-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_models', '0005_auto_20211122_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
