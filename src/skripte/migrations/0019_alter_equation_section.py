# Generated by Django 3.2.6 on 2021-10-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0018_alter_equation_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='section',
            field=models.ManyToManyField(blank=True, related_name='equations', to='skripte.Section'),
        ),
    ]
