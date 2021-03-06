# Generated by Django 3.2.6 on 2021-10-08 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0009_auto_20211008_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skripta',
            options={},
        ),
        migrations.RemoveField(
            model_name='skripta',
            name='order',
        ),
        migrations.CreateModel(
            name='SkriptaSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_order', models.PositiveIntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skripte.section')),
                ('skripta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skripte.skripta')),
            ],
            options={
                'ordering': ('section_order',),
            },
        ),
    ]
