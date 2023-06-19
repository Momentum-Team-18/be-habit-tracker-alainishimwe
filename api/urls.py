from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('habits/', views.habit_list.as_view(), name='habit-list'),
    path('records/<int:pk>', views.habit_list_record.as_view(), name='habit-list-record'),
    path('createhabit/', views.create_habit.as_view(), name='create-habit'),
    path('createrecord/', views.create_record.as_view(), name='create-record'),
    path('onehabit/<int:pk>', views.one_habit.as_view(), name='one-habit'),
]

urlpatterns = format_suffix_patterns(urlpatterns)