# Generated by Django 3.2.6 on 2021-08-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0019_auto_20210829_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]