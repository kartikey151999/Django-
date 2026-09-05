from django.db import models

# Create your models here.
 
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
