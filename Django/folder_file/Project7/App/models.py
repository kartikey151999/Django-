from django.db import models

# Create your models here.
class Bio(models.Model):
    Id:models.IntegerField()
    Description:models.TextField()
    Location:models.CharField(max_length=100)
    Age:models.IntegerField(2)


    def __str__(self):
        return str(Id)
