# Generated by Django 4.2.2 on 2023-06-05 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0005_alter_habitrecord_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habitrecord',
            old_name='date',
            new_name='created',
        ),
    ]
