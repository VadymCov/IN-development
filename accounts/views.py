from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileEditForm
from django.views import View
from .models import Profiles
from todolist.models import Task
# Create your views here.

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/registry.html'
    success_url = reverse_lazy("accounts:login")

@login_required 
def profile(request):
    profiles = Profiles.objects.all()
    recent_tasks = Task.objects.filter(created_by=request.user).order_by('-create_at')[:3] 
    user_profile = get_object_or_404(Profiles, user=request.user)
    
    return render(request, 'accounts/profile.html', {
        'profiles': profiles,
        'profile': user_profile,
        'title': 'Profiles',
        'recent_tasks': recent_tasks
        })

class ProfileEditView(LoginRequiredMixin, View):
    template_name = 'accounts/edit_profile.html'

    def get(self, request):
        form = ProfileEditForm(user = request.user)
        return render(request, self.template_name, {'form': form, 'title': 'Edit Profile'})
    
    def post(self, request):
        form = ProfileEditForm(user=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('accounts:profile')
        return render(request, self.template_name, {'form':form})