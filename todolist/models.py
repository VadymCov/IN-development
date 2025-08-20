from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField("Task", max_length=200)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"