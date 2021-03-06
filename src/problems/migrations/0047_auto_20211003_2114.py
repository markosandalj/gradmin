# Generated by Django 3.2.6 on 2021-10-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0046_alter_problem_skripta'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='approval',
            field=models.CharField(choices=[('approved', 'Approved'), ('unapproved', 'Unapproved')], default='unapproved', max_length=20),
        ),
        migrations.AlterField(
            model_name='problem',
            name='shop_availability',
            field=models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('hidden', 'Hidden')], default='hidden', help_text='Hidden = problem wont be shown anywhere, Available = it is going to br shown as free preview, Unavailable = wont be shown as a free preivew. Only when bought.', max_length=20),
        ),
    ]
