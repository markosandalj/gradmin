# Generated by Django 3.2.6 on 2021-08-29 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0010_rename_subquestion_question_main_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='correctanswer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.question'),
        ),
    ]
