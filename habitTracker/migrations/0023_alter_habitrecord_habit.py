# Generated by Django 4.2.2 on 2023-06-07 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0022_alter_habitrecord_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitrecord',
            name='habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='habitTracker.habit'),
        ),
    ]
