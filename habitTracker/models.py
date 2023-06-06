from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    birthdate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

class Habit(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    
class HabitRecord(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    achieved = models.CharField(max_length=100, blank=True, null=True )

    def __str__(self):
        return self.achieved