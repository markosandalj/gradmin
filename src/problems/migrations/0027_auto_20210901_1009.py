# Generated by Django 3.2.6 on 2021-09-01 10:09

from django.db import migrations, models
import django.db.models.functions.comparison


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0026_alter_problem_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': [django.db.models.functions.comparison.Cast('question__question_text', models.IntegerField())]},
        ),
        migrations.RemoveField(
            model_name='problem',
            name='order',
        ),
    ]
