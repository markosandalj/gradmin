# Generated by Django 3.2.6 on 2022-07-19 13:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailforms', '0005_alter_formsubmission_form_data'),
        ('wagtailredirects', '0008_add_verbose_name_plural'),
        ('wagmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('course_title', models.CharField(max_length=100, null=True)),
                ('content', wagtail.fields.StreamField([('course_chapters', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title that will be displayed on web', required=True)), ('admin_title', wagtail.blocks.CharBlock(help_text='Title that will be displayed only in admin', required=True)), ('lessons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(max_length=100, required=True))])))]))], blank=True, null=True, use_json_field=None)),
            ],
            options={
                'verbose_name': 'Course Page',
                'verbose_name_plural': 'Course Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='CourseBuilderPage',
        ),
    ]
