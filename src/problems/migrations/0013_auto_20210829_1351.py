# Generated by Django 3.2.6 on 2021-08-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0012_problem_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='section',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='section',
            name='shopify_page_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
