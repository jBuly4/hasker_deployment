# Generated by Django 4.2.3 on 2023-07-20 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasker_app', '0006_alter_postanswer_publish_alter_postquestion_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postanswer',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 11, 39, 34, 419013, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postquestion',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 11, 39, 34, 418495, tzinfo=datetime.timezone.utc)),
        ),
    ]