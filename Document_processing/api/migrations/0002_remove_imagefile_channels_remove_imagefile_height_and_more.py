# Generated by Django 5.0.6 on 2025-01-09 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagefile',
            name='channels',
        ),
        migrations.RemoveField(
            model_name='imagefile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='imagefile',
            name='width',
        ),
        migrations.RemoveField(
            model_name='pdffile',
            name='page_count',
        ),
        migrations.RemoveField(
            model_name='pdffile',
            name='page_height',
        ),
        migrations.RemoveField(
            model_name='pdffile',
            name='page_width',
        ),
    ]
