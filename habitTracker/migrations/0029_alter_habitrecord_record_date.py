# Generated by Django 4.2.2 on 2023-06-08 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0028_habit_target_number_alter_habitrecord_record_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitrecord',
            name='record_date',
            field=models.DateField(default=datetime.date(2023, 6, 8)),
        ),
    ]
