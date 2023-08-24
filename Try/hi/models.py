from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

from django.db import models
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    username=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    email = models.EmailField()
    dob=models.DateField(auto_now=True)
    age = models.IntegerField()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.name

