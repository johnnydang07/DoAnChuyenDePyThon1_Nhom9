# Generated by Django 4.2.5 on 2023-10-14 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postmodel_draft_postmodel_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='publish',
        ),
    ]
