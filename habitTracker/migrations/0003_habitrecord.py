# Generated by Django 4.2.2 on 2023-06-05 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitTracker', '0002_habit'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitTracker.habit')),
            ],
        ),
    ]
