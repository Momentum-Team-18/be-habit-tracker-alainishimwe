from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitRecord
from .forms import HabitForm
# Create your views here.
def homePage(request):
    habits = Habit.objects.all()
    context = {'habits':habits}
    return render(request, 'habitTracker/index.html', context)

def newHabit(request):
    form = HabitForm()
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    return render(request, 'habitTracker/habit_form.html', {'form': form})

def habitDetails(request, pk):
    habitRecord = get_object_or_404(HabitRecord, pk=pk)
    habits = Habit.objects.all()
    context = {'habitRecord' : habitRecord,'habits':habits }

    return render(request, 'habitTracker/habitDetails.html', context)
