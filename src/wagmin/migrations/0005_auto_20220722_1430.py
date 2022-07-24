# Generated by Django 3.2.6 on 2022-07-22 14:30

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagmin', '0004_auto_20220719_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('page_title', models.CharField(max_length=100, null=True)),
                ('content', wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('page_link', wagtail.blocks.PageChooserBlock(required=True))])))]))], use_json_field=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='coursechapter',
            name='chapter_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coursechapter',
            name='lessons',
            field=wagtail.fields.StreamField([('lesson_video', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title that will be displayed on web', required=True)), ('admin_title', wagtail.blocks.CharBlock(help_text='Title that will be displayed only in admin', required=True)), ('lessons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('lesson_problem_solution', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title that will be displayed on web', required=True)), ('admin_title', wagtail.blocks.CharBlock(help_text='Title that will be displayed only in admin', required=True)), ('lessons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('lesson_quiz', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title that will be displayed on web', required=True)), ('admin_title', wagtail.blocks.CharBlock(help_text='Title that will be displayed only in admin', required=True)), ('lessons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('lesson_page_content', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title that will be displayed on web', required=True)), ('admin_title', wagtail.blocks.CharBlock(help_text='Title that will be displayed only in admin', required=True)), ('lessons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('lesson_interactive_map', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title that will be displayed on web', required=True)), ('admin_title', wagtail.blocks.CharBlock(help_text='Title that will be displayed only in admin', required=True)), ('lessons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(max_length=100, required=True))])))]))], use_json_field=None),
        ),
    ]