# Generated by Django 3.2.6 on 2021-11-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0049_correctanswer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerchoice',
            name='choice_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]