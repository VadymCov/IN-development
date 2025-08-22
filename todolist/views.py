from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Task
# Create your views here.

def index(request):
    task = Task.objects.all()
    print(f"{task.query}")

    return render(request, 'todolist/index.html', {'tasks': task, 'title': 'Todo List'})

@require_POST
def add(request):
    task_name = request.POST.get("task_name")
    if len(task_name) > 5:
        Task.objects.create(title=task_name)
    return redirect('index')

def update(request, task_id):
    task_name = Task.objects.get(id=task_id)
    task_name.is_complete = not task_name.is_complete
    task_name.save()
    return redirect('index')

def delete(request, task_id):
    task_name = Task.objects.get(id=task_id)
    task_name.delete()
    return redirect('index')


