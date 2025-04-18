# Generated by Django 3.0.4 on 2020-04-17 18:36

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20200417_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 14, 36, 5, 866269)),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
