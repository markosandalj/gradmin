# Generated by Django 3.2.6 on 2021-08-29 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0011_correctanswer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.section'),
        ),
    ]