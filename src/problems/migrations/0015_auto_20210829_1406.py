# Generated by Django 3.2.6 on 2021-08-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0014_auto_20210829_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answerchoice',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='answerchoice',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
