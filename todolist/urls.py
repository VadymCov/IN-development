
from django.urls import path
from todolist import views

app_name = 'todolist'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('index/', views.index, name='index'),
    path('task_add_form/', views.task_add_form, name='task_add_form'),
    path('add/', views.add, name='add'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    ]