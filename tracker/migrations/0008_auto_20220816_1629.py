# Generated by Django 2.2 on 2022-08-16 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20220816_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 16, 16, 29, 51, 664555)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_time',
            field=models.TimeField(default=datetime.time(16, 29, 51, 664555)),
        ),
    ]