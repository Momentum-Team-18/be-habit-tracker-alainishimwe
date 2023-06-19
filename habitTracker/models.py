from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# USER_TYPES = [
#     ("Habit_Creator", "Habit_Creator"),
#     ("Habit_Observor", "Habit_Observor"),
# ]
class User(AbstractUser):
    birthdate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    # Type_of_user = models.CharField(max_length=100, choices=USER_TYPES, null=True)

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    target_number = models.IntegerField(default=0, null=False )
    def __str__(self):
        return self.name
    
class HabitRecord(models.Model):
    
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='HabitRecords')


    record_date = models.DateField(auto_now_add=False, auto_now=False, blank=False, null=False, default=timezone.now)
    achieved = models.IntegerField(default=0, null=False )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['habit','record_date'], name='unique_constr'
            )
        ]
        ordering = ['record_date']

    def __str__(self):
        return f'{self.habit} on {self.record_date}'
