# Generated by Django 4.2.2 on 2023-06-08 01:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0027_alter_habitrecord_achieved'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='target_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='habitrecord',
            name='record_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 1, 10, 16, 397360)),
        ),
    ]
