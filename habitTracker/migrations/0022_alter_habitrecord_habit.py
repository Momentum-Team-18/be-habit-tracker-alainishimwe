# Generated by Django 4.2.2 on 2023-06-07 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0021_remove_habitrecord_user_habit_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitrecord',
            name='habit',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='habitTracker.habit'),
            preserve_default=False,
        ),
    ]
