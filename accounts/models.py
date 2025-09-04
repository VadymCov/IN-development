from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Q

# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        full_name = self.user.get_full_name()
        if full_name:
            return f"{self.user.username} {full_name}"
        return self.user.username
    
    @property
    def task_stats(self):
        from todolist.models import Task

        return Task.objects.filter(created_by=self.user).aggregate(
            total=Count('id'),
            completed=Count('id', filter=Q(is_complete=True)),
            not_completed=Count('id', filter=Q(is_complete=False))

        )
    
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance)
        