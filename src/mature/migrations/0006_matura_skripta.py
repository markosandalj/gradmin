# Generated by Django 3.2.6 on 2021-11-03 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0028_skripta_file'),
        ('mature', '0005_matura_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='matura',
            name='skripta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skripte.skripta'),
        ),
    ]
