from django import forms 
from .models import Habit, HabitRecord

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'target')


class HabitRecordForm(forms.ModelForm):
    class Meta:
        model= HabitRecord
        fields = ('record_date', 'achieved')