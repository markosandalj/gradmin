# Generated by Django 3.2.6 on 2021-11-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0028_skripta_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='exclude',
            field=models.BooleanField(default=False),
        ),
    ]
