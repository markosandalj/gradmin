# Generated by Django 3.2.6 on 2021-09-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0023_auto_20210829_2205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='problem',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]