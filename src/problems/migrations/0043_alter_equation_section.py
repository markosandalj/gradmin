# Generated by Django 3.2.6 on 2021-09-23 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0042_auto_20210920_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='section',
            field=models.ManyToManyField(blank=True, to='problems.Section'),
        ),
    ]