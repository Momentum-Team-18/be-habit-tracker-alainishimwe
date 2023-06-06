# Generated by Django 4.2.2 on 2023-06-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
