# Generated by Django 4.2.2 on 2023-06-07 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0019_alter_habit_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='user',
        ),
        migrations.AddField(
            model_name='habitrecord',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]