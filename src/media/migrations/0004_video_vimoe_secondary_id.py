# Generated by Django 3.2.6 on 2021-10-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20211007_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='vimoe_secondary_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
