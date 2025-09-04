from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    title = models.CharField("Task", max_length=200)
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"