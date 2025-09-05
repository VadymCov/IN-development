from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from todolist.models import Task
from .forms import RegisterForm
from .models import Profiles
# Create your views here.

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/registry.html'
    success_url = reverse_lazy("accounts:login")

@login_required 
def profile(request):
    profiles = Profiles.objects.all()
    recent_tasks = Task.objects.filter(created_by=request.user).order_by('-create_at')[:3] 
    
    return render(request, 'accounts/profile.html', {
        'profiles': profiles,
        'title': 'Profiles',
        'recent_tasks': recent_tasks
        })

