# Generated by Django 3.2.6 on 2021-10-29 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_models', '0004_rename_template_sufix_template_template_suffix'),
        ('skripte', '0020_auto_20211029_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='skripta',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopify_models.page'),
        ),
    ]