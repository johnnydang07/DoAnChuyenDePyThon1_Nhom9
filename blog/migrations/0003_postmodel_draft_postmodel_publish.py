# Generated by Django 4.2.5 on 2023-10-13 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_post_profile_alter_comment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 10, 13, 3, 21, 2, 418525, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]