# Generated by Django 3.2.6 on 2022-04-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0016_image_image_dark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
