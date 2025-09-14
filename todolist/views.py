from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .models import Task

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home_page.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todolist:index')
        return super().dispatch(request, *args, **kwargs)

@login_required
def index(request):
    tasks = Task.objects.filter(created_by=request.user)
    print(f"This is task query >>>>{tasks.query}")
    return render(request, 'todolist/index.html', {'tasks': tasks, 'title': 'Profiles'})

def task_add_form(request):
    tasks = Task.objects.filter(created_by=request.user)
    print(f"This is task query >>>>{tasks.query}")
    return render(request, 'todolist/task_add.html', {'tasks': tasks, 'title': 'My tasks'})

@require_POST
@login_required
def add(request):
    task_name = request.POST.get("task_name")
    if len(task_name) > 5:
        Task.objects.create(title=task_name, created_by=request.user)
    return redirect('todolist:task_add_form')

@require_POST
def update(request, task_id):
    task_name = Task.objects.get(id=task_id)
    task_name.is_complete = not task_name.is_complete
    task_name.save()
    return redirect('todolist:task_add_form')

@require_POST
def delete(request, task_id):
    task_name = Task.objects.get(id=task_id)
    task_name.delete()
    return redirect('todolist:task_add_form')

