# Generated by Django 3.0.4 on 2020-04-18 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20200417_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 18, 13, 7, 7, 660626)),
        ),
    ]
