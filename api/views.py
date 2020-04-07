from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todo

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/task-list/',
    'Detail view': '/task-detail/<str:pk>/',
    'Create': '/task-create/',
    'Update': '/task-update/<str:pk>/',
    'Delete': '/task-delete/<str:pk>/',
  }

  return Response(api_urls)

@api_view(['GET'])
def todoList(request):
  task = Todo.objects.all()
  serializer = TodoSerializer(task, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
  task = Todo.objects.get(id=pk)
  serializer = TodoSerializer(task, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
  serializer = TodoSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)


@api_view(['GET', 'POST'])
def todoUpdate(request, pk):
  task = Todo.objects.get(id=pk)
  serializer = TodoSerializer(instance=task, data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
  task = Todo.objects.get(id=pk)
  task.delete()

  return Response('Item has been deleted!')
