# Generated by Django 4.2.2 on 2023-06-08 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0029_alter_habitrecord_record_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitrecord',
            name='record_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 13, 11, 59, 568344, tzinfo=datetime.timezone.utc)),
        ),
    ]
