# Generated by Django 3.2.6 on 2021-09-07 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0028_problem_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_choices', to='problems.question'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='matura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='problems', to='problems.matura'),
        ),
    ]
