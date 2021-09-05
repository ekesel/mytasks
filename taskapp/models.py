from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-pk']
        verbose_name_plural = "Task Manager"
    