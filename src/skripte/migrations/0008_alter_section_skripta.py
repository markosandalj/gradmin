# Generated by Django 3.2.6 on 2021-10-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0007_alter_section_shopify_page_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='skripta',
            field=models.ManyToManyField(blank=True, related_name='sections', to='skripte.Skripta'),
        ),
    ]
