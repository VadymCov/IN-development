from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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