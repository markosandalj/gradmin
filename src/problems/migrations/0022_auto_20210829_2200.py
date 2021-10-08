# Generated by Django 3.2.6 on 2021-08-29 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0021_alter_video_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.question'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='video_solution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.video'),
        ),
    ]