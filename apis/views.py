from django.shortcuts import render
from  rest_framework import generics
from  rest_framework.response import Response  
from  rest_framework.decorators import api_view 
from todos import models
from .serializers import TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
@api_view(['GET'])
def getdata(request,pk):
    queryset = models.Todo.objects.get(id=pk)
    serializer = TodoSerializer(queryset)
    print(serializer.data)
    return Response(serializer.data)