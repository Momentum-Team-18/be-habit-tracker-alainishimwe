from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitRecord, User
from .forms import HabitForm, HabitRecordForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models.functions import Round
import math
# Create your views here.

@login_required
def homePage(request):
    habits = Habit.objects.all()
    habitRecords = HabitRecord.objects.all()
    context = {'habits':habits, 'habitRecords':habitRecords}
    return render(request, 'habitTracker/index.html', context)
@login_required
def newHabit(request):
    form = HabitForm()
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('homePage')
    return render(request, 'habitTracker/habit_form.html', {'form': form})

def newRecord(request,pk):
    form = HabitRecordForm()
    # habitRecords = HabitRecord.objects.all()
    habit = get_object_or_404(Habit, id=pk)
    if request.user != habit.user:
        return HttpResponse("Not allowed here")
    
    context = {'form': form, 'habit':habit}
    if request.method == 'POST':
        form= HabitRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()

            return redirect('habitDetails', pk)
    return render(request, 'habitTracker/daily_record_form.html', context )

def editRecord(request,pk):
    record = get_object_or_404(HabitRecord,pk=pk)
    habit_pk = record.habit_id
    if request.user != record.habit.user:
        return HttpResponse("Not allowed to edit")
    
    if request.method == "POST":
        form = HabitRecordForm(request.POST, instance=record)
        if form.is_valid():
            record=form.save(commit=False)
            record.save()
            return redirect('habitDetails', habit_pk)
    else:
        form = HabitRecordForm(instance=record)
    return render (request, 'habitTracker/daily_record_form.html', {'form':form} )

def deleteRecord(request, pk):
    record = get_object_or_404(HabitRecord,pk=pk)
    habit_pk = record.habit_id

    if request.user != record.habit.user:
        return HttpResponse("Not allowed to delete")
    record.delete()
    return redirect('habitDetails', habit_pk)


def habitDetails(request,pk):
    habit = get_object_or_404(Habit, pk=pk)
    record = HabitRecord.objects.filter(habit_id=pk)
    average = record.aggregate((Avg('achieved')))
    average_numb = math.floor(average['achieved__avg'])
    context = {'habit':habit, 'record':record, 'average_numb':average_numb }

    return render(request, 'habitTracker/habitDetails.html', context)


def dailyRecord(request, pk):
    records = HabitRecord.objects.filter(record_date=pk)
    
    id_for_habits = Habit.objects.values_list('id', flat=True) 
    # record = get_object_or_404(HabitRecord, record_date=pk)
    
    context = { 'records': records, 'id_for_habits': id_for_habits}

    return render(request, 'habitTracker/record_Details.html', context)



