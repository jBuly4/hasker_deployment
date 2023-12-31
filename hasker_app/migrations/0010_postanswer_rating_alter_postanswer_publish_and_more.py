# Generated by Django 4.2.3 on 2023-07-20 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasker_app', '0009_postquestion_rating_alter_postanswer_publish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postanswer',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postanswer',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 15, 6, 38, 15238, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postquestion',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 15, 6, 38, 14751, tzinfo=datetime.timezone.utc)),
        ),
    ]
