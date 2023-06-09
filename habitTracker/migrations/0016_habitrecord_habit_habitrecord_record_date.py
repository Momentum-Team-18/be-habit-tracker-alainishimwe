# Generated by Django 4.2.2 on 2023-06-06 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0015_remove_habitrecord_record_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitrecord',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habitTracker.habit'),
        ),
        migrations.AddField(
            model_name='habitrecord',
            name='record_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
