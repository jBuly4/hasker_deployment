# Generated by Django 4.2.3 on 2023-07-22 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasker_app', '0012_tag_alter_postanswer_publish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postanswer',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 22, 17, 35, 37, 13617, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postquestion',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 22, 17, 35, 37, 12678, tzinfo=datetime.timezone.utc)),
        ),
    ]
