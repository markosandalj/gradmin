# Generated by Django 3.2.6 on 2021-11-03 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0012_svg'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='svg',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
