# Generated by Django 3.2.6 on 2021-12-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0029_section_exclude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='related_equation',
            field=models.ManyToManyField(blank=True, null=True, related_name='_skripte_equation_related_equation_+', to='skripte.Equation'),
        ),
    ]
