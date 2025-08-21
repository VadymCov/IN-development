from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Task
# Create your views here.

def index(request):
    task = Task.objects.all()
    return render(request, 'todolist/index.html', {'task': task, 'title': 'Todo List'})

@require_POST
def add(request):
    task_name = request.POST.get("task_name")
    Task.objects.create(title = task_name)
    return redirect('index')