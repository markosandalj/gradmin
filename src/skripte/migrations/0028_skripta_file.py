# Generated by Django 3.2.6 on 2021-11-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0014_auto_20211103_1208'),
        ('skripte', '0027_auto_20211030_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='skripta',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media.pdf'),
        ),
    ]
