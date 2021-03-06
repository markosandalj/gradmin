# Generated by Django 3.2.6 on 2021-09-20 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0041_auto_20210920_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='equation',
            name='section',
            field=models.ManyToManyField(blank=True, null=True, to='problems.Section'),
        ),
        migrations.AddField(
            model_name='equation',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.subject'),
        ),
    ]
