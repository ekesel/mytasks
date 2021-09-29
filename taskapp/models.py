from django.db import models
from django.contrib.auth.models import User
# Create your models here.

types = (
    ('Daily','Daily'),
    ('Normal','Normal'),
)

class tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    check = models.BooleanField(default=False)
    types = models.CharField(choices=types,default='Normal',max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-pk']
        verbose_name_plural = "Task Manager"
    
class streak(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.IntegerField()