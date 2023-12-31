# Generated by Django 4.2.3 on 2023-07-31 18:42

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hasker_app', '0017_postanswer_users_like_postquestion_users_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postanswer',
            name='users_dislike',
            field=models.ManyToManyField(blank=True, related_name='answers_disliked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postquestion',
            name='users_dislike',
            field=models.ManyToManyField(blank=True, related_name='questions_disliked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postanswer',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 31, 18, 42, 31, 506757, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postquestion',
            name='publish',
            field=models.DateField(default=datetime.datetime(2023, 7, 31, 18, 42, 31, 505244, tzinfo=datetime.timezone.utc)),
        ),
    ]
