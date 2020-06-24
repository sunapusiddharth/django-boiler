from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import ToDoSerializer

# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=ToDoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class=ToDoSerializer