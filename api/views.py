from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework.generics import ListCreateApiView, RetrieveUpdateDestroyApiView
from .serializers import TaskSerializer, EmployeeSerializer
from .models import Task, Employee
# Create your views here.


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-update/<str:pk>/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['Post'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Post'])
def taskUpdate(request, pk):

    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Delete'])
def taskDelete(request, pk):

    task = Task.objects.get(id=pk)
    task.delete()
    return Response('item successfully delete!!')


@api_view(['GET'])
def employeeList(request):
    tasks = Employee.objects.all()
    serializer = EmployeeSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def employeeDetail(request, pk):
    tasks = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['Post'])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Post'])
def employeeUpdate(request, pk):

    task = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Delete'])
def employeeDelete(request, pk):

    task = Employee.objects.get(id=pk)
    task.delete()
    return Response('item successfully delete!!')
