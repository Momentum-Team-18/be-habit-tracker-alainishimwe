# Generated by Django 4.2.2 on 2023-06-06 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0014_remove_habit_user_remove_habitrecord_habit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitrecord',
            name='record_date',
        ),
    ]
