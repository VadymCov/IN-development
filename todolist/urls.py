
from django.urls import path
from todolist import views

urlpatterns = [
    path('index/', views.index, name='index')
]
