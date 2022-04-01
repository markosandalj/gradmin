# Generated by Django 3.2.6 on 2022-03-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mature', '0007_alter_year_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='term',
            field=models.CharField(choices=[('ljeto', 'Ljetni rok'), ('jesen', 'Jesenski rok'), ('zima', 'Zimski rok'), ('ogledna', 'Ogledni ispit')], max_length=7, unique=True),
        ),
    ]