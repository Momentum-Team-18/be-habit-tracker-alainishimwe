from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitRecord
from .forms import HabitForm, HabitRecordForm
# Create your views here.
def homePage(request):
    habits = Habit.objects.all()
    habitRecords = HabitRecord.objects.all()
    context = {'habits':habits, 'habitRecords':habitRecords}
    return render(request, 'habitTracker/index.html', context)

def newHabit(request):
    form = HabitForm()
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    return render(request, 'habitTracker/habit_form.html', {'form': form})

def newRecord(request,pk):
    form = HabitRecordForm()
    # habitRecords = HabitRecord.objects.all()
    habit = get_object_or_404(Habit, id=pk)

    context = {'form': form, 'habit':habit}
    if request.method == 'POST':
        form= HabitRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()

            return redirect('habitDetails', pk)
    return render(request, 'habitTracker/daily_record_form.html', context )

def habitDetails(request,pk):
    habit = get_object_or_404(Habit, pk=pk)
    
    context = {'habit':habit }

    return render(request, 'habitTracker/habitDetails.html', context)
