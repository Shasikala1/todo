from django.db import models

class Task(models.Model):
    task=models.CharField(max_length=250)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True) #only once created at starting
    updated_at=models.DateField(auto_now=True) #everytime when u update 

# Create your models here.
    def __str__(self):
        return self.task