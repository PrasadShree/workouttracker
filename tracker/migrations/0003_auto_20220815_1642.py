# Generated by Django 2.2 on 2022-08-15 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20220815_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='date_of_workout',
            field=models.DateField(default=datetime.datetime(2022, 8, 15, 16, 42, 54, 304326)),
        ),
        migrations.AddField(
            model_name='exercise',
            name='time_of_workout',
            field=models.TimeField(default=datetime.time(16, 42, 54, 304326)),
        ),
    ]
