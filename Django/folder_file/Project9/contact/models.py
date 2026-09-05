from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    contactNumber = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
