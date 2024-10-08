from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    birth = models.DateField()
    gender = models.CharField(max_length=10, null=True, blank=True)
    introductions = models.TextField(null=True, blank=True)