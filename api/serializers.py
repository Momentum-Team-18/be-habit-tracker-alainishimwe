from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from habitTracker.models import Habit, HabitRecord, User

class HabitSerializer(serializers.ModelSerializer):
    HabitRecords = serializers.HyperlinkedRelatedField(many=True,view_name='habit-list-record', read_only=True)
    user = serializers.ReadOnlyField(source='user.username') 
    class Meta:
        model = Habit
        fields = ['user','name','target','target_number', 'HabitRecords']

class HabitRecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HabitRecord
        fields = ['habit','record_date', 'achieved' ]

class UserSerializer(serializers.ModelSerializer):
    habits = serializers.PrimaryKeyRelatedField(many=True, queryset=Habit.objects.all())


    class Meta:
        model = User
        fields = ['username', 'habits']