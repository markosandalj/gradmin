# Generated by Django 3.2.6 on 2021-09-29 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0043_alter_equation_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='main_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subquestions', to='problems.question'),
        ),
        migrations.CreateModel(
            name='Skripta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('level', models.CharField(choices=[('A', 'Viša razina'), ('B', 'Niža razina'), ('0', 'Nema razine')], default='0', max_length=2)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.subject')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='skripta',
            field=models.ManyToManyField(blank=True, to='problems.Skripta'),
        ),
    ]
