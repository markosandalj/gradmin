# Generated by Django 3.2.6 on 2021-08-29 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20210827_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CorrectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(blank=True, null=True)),
                ('answer_choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.answerchoice')),
            ],
        ),
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('equation', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('related_equation', models.ManyToManyField(related_name='_problems_equation_related_equation_+', to='problems.Equation')),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('A', 'Viša razina'), ('B', 'Niža razina')], default='A', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('vimeo', models.IntegerField()),
                ('vimeo_edit_link', models.URLField()),
                ('vimeo_view_link', models.URLField()),
                ('vimeo_embed_link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='availability',
        ),
        migrations.AddField(
            model_name='problem',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.question'),
        ),
        migrations.AddField(
            model_name='problem',
            name='shop_availability',
            field=models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('hidden', 'Hidden')], default='hidden', help_text='Hidden = problem wont be shown anywhere', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='subquestion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.question'),
        ),
        migrations.AddField(
            model_name='matura',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='problems.subject'),
        ),
        migrations.AddField(
            model_name='matura',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='problems.term'),
        ),
        migrations.AddField(
            model_name='matura',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='problems.year'),
        ),
        migrations.AddField(
            model_name='hint',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem'),
        ),
        migrations.AddField(
            model_name='answerchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.question'),
        ),
        migrations.AddField(
            model_name='problem',
            name='matura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.matura'),
        ),
        migrations.AddField(
            model_name='problem',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.subject'),
        ),
        migrations.AddField(
            model_name='section',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='problems.subject'),
        ),
    ]
