# Generated by Django 3.2.6 on 2022-01-23 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0030_alter_equation_related_equation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='related_equation',
            field=models.ManyToManyField(blank=True, related_name='_skripte_equation_related_equation_+', to='skripte.Equation'),
        ),
    ]