from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from django.core import serializers


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


def getTasks(request):
    allTasks = Task.objects.all()
    _json = serializers.serialize("json", allTasks)

    return HttpResponse(_json, content_type="application/json")
