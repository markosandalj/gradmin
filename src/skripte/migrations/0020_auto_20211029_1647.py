# Generated by Django 3.2.6 on 2021-10-29 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skripte', '0019_alter_equation_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Razred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='section',
            name='shopify_page_id',
        ),
        migrations.RemoveField(
            model_name='section',
            name='shopify_page_url',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('razred', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skripte.razred')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skripte.category'),
        ),
    ]
