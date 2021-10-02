# Generated by Django 3.2.6 on 2021-08-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20210829_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='hint',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='matura',
            name='level',
            field=models.CharField(choices=[('A', 'Viša razina'), ('B', 'Niža razina'), ('0', 'Nema razine')], default='0', max_length=2),
        ),
    ]
