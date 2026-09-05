from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age=models.IntegerField(max_length=2)
    className=models.IntegerField(max_length=1)
    email=models.EmailField(unique=True)

    
    def __str__(self):
        return self.name+" , " + str(self.age) + " , " + str(self.className) + " , " + self.email