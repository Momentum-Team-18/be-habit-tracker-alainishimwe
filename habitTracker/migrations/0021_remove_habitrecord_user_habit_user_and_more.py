# Generated by Django 4.2.2 on 2023-06-07 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0020_remove_habit_user_habitrecord_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitrecord',
            name='user',
        ),
        migrations.AddField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habitrecord',
            name='habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='habitTracker.habit'),
        ),
    ]
