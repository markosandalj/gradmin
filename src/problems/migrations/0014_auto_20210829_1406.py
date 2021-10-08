# Generated by Django 3.2.6 on 2021-08-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0013_auto_20210829_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['order']},
        ),
        migrations.RenameField(
            model_name='section',
            old_name='my_order',
            new_name='order',
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]