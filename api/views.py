
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from habitTracker.models import Habit, HabitRecord, User
from django.contrib.auth.models import AbstractUser
from api.serializers import HabitSerializer, HabitRecordSerializer, UserSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly

# Create your views here.

# @api_view(['GET', 'POST'])
# def habit_list(request, format=None):

#     if request.method == 'GET':
#         habits = Habit.objects.all()
#         serializer = HabitSerializer(habits, context={'request':request}, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = HabitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def habit_list_record(request, pk, format=None):

#     try:
#         habit_record = HabitRecord.objects.get(pk=pk)
#     except HabitRecord.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = HabitRecordSerializer(habit_record, context={'request':request})
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = HabitRecordSerializer(habit_record, data=request.data, context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         habit_record.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class habit_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
    
class one_habit(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Habit.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    serializer_class = HabitSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)
    
class create_habit(mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    
    
class habit_list_record(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = HabitRecord.objects.all()
    serializer_class = HabitRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class create_record(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = HabitRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer