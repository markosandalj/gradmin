# Generated by Django 3.2.6 on 2021-10-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0008_alter_section_skripta'),
        ('problems', '0045_auto_20210930_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='skripta',
            field=models.ManyToManyField(blank=True, related_name='problems', to='skripte.Skripta'),
        ),
    ]
