from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email = models.EmailField()
    dob=models.DateField(auto_now=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

