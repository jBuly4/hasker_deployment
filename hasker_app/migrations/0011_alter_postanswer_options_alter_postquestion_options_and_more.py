# Generated by Django 4.2.3 on 2023-07-20 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasker_app', '0010_postanswer_rating_alter_postanswer_publish_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postanswer',
            options={'ordering': ['rating', '-publish']},
        ),
        migrations.AlterModelOptions(
            name='postquestion',
            options={'ordering': ['rating', '-publish']},
        ),
        migrations.AlterField(
            model_name='postanswer',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 15, 16, 24, 237931, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postquestion',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 15, 16, 24, 237432, tzinfo=datetime.timezone.utc)),
        ),
    ]