from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('create/', views.newHabit, name='newHabit'),
    path('habit/<int:pk>/', views.habitDetails, name='habitDetails'),
]