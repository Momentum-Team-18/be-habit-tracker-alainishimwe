# Generated by Django 4.2.2 on 2023-06-07 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0017_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitrecord',
            name='habit',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='habitTracker.habit'),
            preserve_default=False,
        ),
    ]
