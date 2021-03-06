# Generated by Django 3.2.6 on 2021-09-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mature', '0002_auto_20210930_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='term',
            field=models.CharField(choices=[('ljeto', 'Ljetni rok'), ('jesen', 'Jesenski rok'), ('zima', 'Zimski rok')], max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.IntegerField(choices=[(2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021')], unique=True),
        ),
    ]
