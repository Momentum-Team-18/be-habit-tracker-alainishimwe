# Generated by Django 4.2.2 on 2023-06-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0004_alter_habitrecord_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitrecord',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
