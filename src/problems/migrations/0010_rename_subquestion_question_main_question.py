# Generated by Django 3.2.6 on 2021-08-29 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0009_auto_20210829_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='subquestion',
            new_name='main_question',
        ),
    ]
